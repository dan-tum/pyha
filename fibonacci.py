# -*- coding: utf-8 -*-
"""
Created on Fri May  8 01:18:06 2015

@author: Daniel
"""

def fibonacci(n):
    
    f1 = 1
    f2 = 1
    print "f1 = %s" %f1
    print "f2 = %s" %f2
    i = 2
    
    for x in range(0, n-2):
        
        fn = f1 + f2
        f1 = f2
        f2 = fn
        i = i + 1
        print "f" + str(i) + " = %s" %fn



test = fibonacci(30)