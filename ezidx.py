#idx: index
#hidx: handle of index
import random

g_idx_dict = {"int hash":"int count"}

def get_handle(init_idx=0):
    #get a handle in random int(128)
    #each handle can use to its own index stuff
    global g_idx_dict
    hidx = random.getrandbits(128)
    if hidx in g_idx_dict:
        hidx = get_handle(init_idx)
    g_idx_dict.setdefault(hidx, init_idx)
    return hidx

def clear():
    #clear all index data
    global g_idx_dict
    g_idx_dict.clear()
    return True

def remove(hidx=None):
    #remove the handle of index
    global g_idx_dict
    if hidx == None or hidx not in g_idx_dict:
        return False
    g_idx_dict.pop(hidx)
    return True

def idx(hidx=None):
    #get the current index and will increase 1 for next time
    global g_idx_dict
    if hidx == None or hidx not in g_idx_dict:
        return False
    cur_idx = g_idx_dict[hidx]
    g_idx_dict[hidx] += 1
    return cur_idx
                
def current_idx(hidx=None):
    #get current index without increase 1 to the index 
    global g_idx_dict
    if hidx == None or hidx not in g_idx_dict:
        return False
    return g_idx_dict[hidx]

def set_idx(hidx, new_idx=0):
    #set hidx's index
    global g_idx_dict
    if hidx == None or hidx not in g_idx_dict:
        return False
    g_idx_dict[hidx] = new_idx
    return True
