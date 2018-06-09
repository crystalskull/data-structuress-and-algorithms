#!/usr/bin/env python3

import gcd

def lcm(a, b):
	'''
	Computes LCM of two numbers
	'''

	g = gcd.gcd(a, b)
	return (a/g) * b
