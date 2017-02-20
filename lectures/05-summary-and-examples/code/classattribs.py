#!/usr/bin/env python3 
#-*- coding: utf-8 -*-

"""
@John Markus Bjørndalen 

This short example demonstrates how class attributes work. 
Take a look at the code and try to predict the output before 
you read further in the comments. 

The main insight needed to understand the code is that 
python searches for attributes that we try to access.
The search order is as follows: 
1) the object itself
2) the class of the object
3) parent classes of the object

If you want to see how Python handles multiple inheritance, 
please see 9.5.1 Multiple Inheritance in 
  http://docs.python.org/2/tutorial/classes.html
or
  https://docs.python.org/3/tutorial/classes.html
"""

class TV:
    _foovar1 = 42

    def __init__(self):
        self._foo2 = 2
        self.__bar = 3


t = TV()

print(t._foovar1, TV._foovar1)
t._foovar1 = 3
print(t._foovar1, TV._foovar1)
TV._foovar1 = 92
print(t._foovar1, TV._foovar1)
