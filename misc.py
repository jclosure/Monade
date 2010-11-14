#
#  misc.py
#  Monade
#
#  Created by Jeremy McMillan on 8/9/10.
#  Copyright (c) 2010 Jeremy McMillan. All rights reserved.
#

def dict_to_attr(target_object, settings, filter=None):
	"""
	Blindly sets object attributes to values of a dictionary (like kwargs)
		with keys of same name.
	Optionally takes a second argument as an iterable to enumerate the keys
		and order on which to set attribute values.
	"""
	
	if not filter:
		# Try everything by default
		filter = settings.keys()
	
	if '__setattr__' in target_object.__dict__:
		setter = lambda t: target_object.__setattr__(t[0],t[1])
	else:
		setter = lambda t: target_object.__dict__.__setitem__(t[0],t[1])
	
	map(setter, [(key,settings[key]) for key in filter if key in settings.keys()])


def perm(items, n=None):
	if n is None:
		n = len(items)
	for i in range(len(items)):
		v = items[i:i+1]
		if n == 1:
			yield v
		else:
			rest = items[:i] + items[i+1:]
			for p in perm(rest, n-1):
				yield v + p

def comb(items, n=None):
	if n is None:
		n = len(items)
	for i in range(len(items)):
		v = items[i:i+1]
		if n == 1:
			yield v
		else:
			rest = items[i+1:]
			for c in comb(rest, n-1):
				yield v + c

def prd(factors):
	"""
	Returns the arithmetic product of an iterable sequence of factors.
	prd([2,3,5]) --> (2 * 3 * 5)
	"""
	return reduce(lambda x,y: x*y,factors)
