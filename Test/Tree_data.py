# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 17:20:57 2018
TREE ABSTRACTION
@author: Kan
"""

def tree(label, branches = []):
    """
    Tree constructor
    A TREE have its LABEL and list of its BRANCHES
    By default branches[] is emprty so we get a leaf
    """                            
    for branch in branches:
        assert is_tree(branch), 'branches must be trees' 
        # is this BRANCH a tree ( verify the tree definition)
    return [label] + list(branches) 
    # return LABEL and list of BRANCHES 
    # list(branches) is to make sure the input argument is converted to LIST 



def label(tree):
    """
    Label selector
    Label is a selector that returns the element at index 0 
    in the list representation of the tree
    """
    return tree[0]

def branches(tree):
    """
    Branch selector
    And Branches are the rest of the list elements
    """
    return tree[1:]


def is_tree(tree):
    """
    How do we know if a branch is a tree.
    It has to be a list.
    It has to have at least one element for the label
    So if that's not true we'll return false
    
    AND
    
    All of its BRANCHES are also need to be TREE
    so in fact is_tree is a tree recursive function itself that goes
    through every branch and the branches of the tree if one of the branches is
    not a TREE then it's not a TREE.
    
    IF EVERY BRANCHES IS A TREE THEN IS MUST BE A TREE
    """
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """
    To check if a tree is in fact just a leaf 
    which checks that the branches are empty an EMPTY LIST -> that's a False value
    and not False return to True: is a leaf
    """
    return not branches(tree)

######### TRE PROCESSING ##################################
    
def fib_tree(n):
    

