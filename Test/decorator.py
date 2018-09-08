# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 04:32:24 2018

@author: Kan
"""

def greet(name):
    return "hello " + name

def greet2(name):
    def get_message():
        return "Hello "
    
    result = get_message() + name
    return result

# Higher order function: A function take a function as an argument or return
# a function or both


def get_text(name):
    return "lorem ipsum, {0} dolor sit met".format(name)

def p_decorate(func):
    def func_wrapper(name):
        return "<p>{0}</p>".format(func(name))
    return func_wrapper

my_get_text = p_decorate(get_text)
print (my_get_text("John"))