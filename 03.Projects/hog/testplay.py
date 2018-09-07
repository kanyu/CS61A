# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 21:26:31 2018

@author: Kan
"""
from random import randint
score0 = 0
score1 = 0

def play(score0, score1, turn):
    i, k = score0, score1
    roll = 1
    while score0 < 100 and score1 < 100:
        roll0 = 0
        roll1 = 0
        turn0 = turn + randint(1, 5)
        turn1 = turn + randint(1, 6)
        print("--------------------------------------------------------")
        print("START TURN", roll, ": ", "p0 :", turn0, "---- p1 :", turn1)
        print("P1 SCORE ================")
        while i <= 100 and roll0 < turn0:
            score0 += 3
            i = score0
            roll0 += 1
            print("         score0", roll0, ":",score0)
        if score0 >= 100 or score1 >= 100:
            break
        print("P2 SCORE ================")
        while k <= 100 and roll1 < turn1:
            score1 += 50
            k = score1
            roll1 += 1
            print("         score1", roll1, ":", score1)
        if score0 >= 100 or score1 >= 100:
            break
        print("END TURN", roll, ": s0---s1 :", score1, "---", score1)
        print("--------------------------------------------------------")
        roll += 1
    return score0, score1
x = 4
y = 5
z = 0
def swap_it():
    global x, y, z
    z = x
    x = y
    y = z
#n = 4
#while n < 10:
#    n + 4
#    print(n)