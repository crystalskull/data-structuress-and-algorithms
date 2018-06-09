#!/usr/bin/env python3

def gcd(a, b):
	'''
	Calculates GCD of two numbers using
	Euclid's algorithm
	'''
	if b == 0:
		return a
	else:
		return gcd(b, a % b)
