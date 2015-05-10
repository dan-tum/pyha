# -*- coding: utf-8 -*-
"""
Created on Thu May  7 10:10:15 2015

@author: Daniel
"""
def deduplicate(entries):
        list = []
        
        for i in entries:
            a = i in list
                
            if a == False:
                    list.append(i)

        
        return list


abc = [0, 1, 2, 2, 3, 4, 5, 1, 3 ,"d", "g", "q", "q", "r"]

print deduplicate(abc)
