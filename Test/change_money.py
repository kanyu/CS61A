# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 00:30:38 2018

@author: Kan
"""

L = [0, 1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]
def change_money(n, L):
    def _change(n, m, i):
        if n == 0:
            return 1
        elif n < 0:
            return 0
        elif m == 0:
            return 0
        else:
            cur = L[len(L)- i - 1]
            nex = L[len(L)- i - 2]
            return _change(n-cur,cur, i) + _change(n, nex, i + 1)   
    return _change(n, L[len(L)- 1], 0)

#d = count_partitions(5, 4)
print(change_money(5000, L))
    