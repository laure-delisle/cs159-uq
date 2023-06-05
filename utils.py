''' Utils:
    - create sets of IDs with certain characteristics
    - plotting methods

'''
import os
import pickle ##change to feather when refactor
from dataset import get_labels, label_to_id
from dataset import forest_labels, water_labels, bare_labels, mine_labels
from dataset import forest_ids, water_ids, bare_ids, mine_ids

def intersection(cat_labels, img_labels):
    return list(set(cat_labels) & set(img_labels))

# core
def has_X(img, labels):
    img_labels = get_labels(img)
    if intersection(labels, img_labels):
        return True
    else: return False

# facades
def has_forest(img):
    return has_X(img, forest_labels)

def has_water(img):
    return has_X(img, water_labels)

def has_bare(img):
    return has_X(img, bare_labels)
    
def has_mine(img):
    return has_X(img, mine_labels)

## Load susbet id lists from pickle if existing, otherwise create
def load_from_pickle(list_name, archive_root=''):
    file_path = os.path.join(archive_root, '{}.pkl'.format(list_name))
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            id_list = pickle.load(f)
        return id_list
    else:
        return None