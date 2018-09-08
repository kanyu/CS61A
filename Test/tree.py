#def tree(root_label, branches=[]):
#    for branch in branches:
#        assert is_tree(branch), 'branches must be trees'
#    return [root_label] + list(branches)
#
#def label(tree):
#    return tree[0]
#
#def branches(tree):
#    return tree[1:]
#
#def is_tree(tree):
#    if type(tree) != list or len(tree) < 1:
#        return False
#    for branch in branches(tree):
#        if not is_tree(branch):
#            return False
#    return True
#
#def is_leaf(tree):
#    return not branches(tree)
#
#def calSquare(n):
#    return n*n
#
#def add_lists(list1, list2):
#    return list(map((lambda n1, n2: n1 + n2), list1, list2))
#
#def hamming_dis(list1, list2):
#    count = 0
#    for n in add_lists(list1, list2):
#        if n == 1:
#            count += 1
#    return count
#
#list1 = [1, 0, 0, 1, 1, 1, 0]
#list2 = [1, 1, 1, 0, 1, 1, 1]
#print(add_lists(list1, list2))
#print(hamming_dis(list1, list2))
#print(sum(list1))

       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        