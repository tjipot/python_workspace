#! /usr/bin/python
# coding=utf8

import math
# import matplotlib.pyplot as plt
# import numpy as np

def sigmoid(x):
    """
    Compute the sigmoid of x:
    :param x: A scalar or numpy array of any size.
    :return: s -- sigmoid(x)
    """
    s = 1/(1+math.exp(-x)); # np

print(sigmoid(0))
print("What A Crazy World!")