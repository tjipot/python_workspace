# -*- coding: utf-8 -*-

L1 = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
	return t[0]

def by_score(t):
	return t[1]

L2 = sorted(L1, key=by_name, reverse=True)
print(L2)

L3 = sorted(L1, key=by_score, reverse=True)
print(L3)