#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''NOV 06, 2016'''

def normalize(name):
    return name.capitalize()        

#测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
