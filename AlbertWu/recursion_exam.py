# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 13:58:32 2018

@author: Kan
"""
#    Subtraction game is a simple game with two players, 
#    player 0 and player 1. At the beginning, there is a pile of n cookies. 
#    The players alternate turns; each turn, a player can take anywhere from 1 to 3 cookies.
#    The player who takes the last cookie wins. Fill in the function can_win, 
#    which returns True if it is possible to win starting at the given number of cookies. 
#    It uses the following ideas:
#    
#    if the number of cookies is negative, it is impossible to win.
#    otherwise, the current player can choose to take either 1, 2, or 3 cookies.
#    evaluate each action: if that action forces the opponent to lose, then return True (since we can win)
#    if none of the actions can force a win, then we can't guarantee a win.


def can_win(number):
    """Returns True if the current player is guaranteed a win
    starting from the given state. It is impossible to win a game
    from an invalid game state.

    >>> can_win (-1) # invalid game state
    False
    >>> can_win (3) # take all three !
    True
    >>> can_win (4)
    False
    """
    "*** YOUR CODE HERE ***"

    if number <= 0:
        return False
    action = 1
    while action <= 3:
        new_state = number - action
        if not can_win ( new_state ):
            return True
        action += 1
    return False
     
can_win(7)
   