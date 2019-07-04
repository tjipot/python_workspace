'''#! /usr/bin/env python3'''
'''NOV 06, 2016'''
'''Concept: Generator In Python'''
import numpy as np

def triangles():
    #result_line = []
    line = 1
    while(True):
        #line = 1
        if(line == 1):
            yield([1])
            line = line + 1
        elif(line == 2):
            yield([1, 1])
            lastline = [1, 1]
            line = line + 1
        else:
            newline = [1]
            tmp = 2
            while tmp < line:
                ele_value = lastline[tmp - 2] + lastline[tmp - 1]
                newline.append(ele_value)
                tmp = tmp + 1
            newline.append(1)
            lastline = newline
            line = line + 1
            yield(newline)

tri = triangles()
n = 10
while n>0:
    print(next(tri))
    n = n - 1

'''n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break'''

