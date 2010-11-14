#
#  facts.py
#  Monade
#
#  Created by Jeremy McMillan on 2/7/10.
#  Copyright (c) 2010 Jeremy McMillan. All rights reserved.
#
from monad import factic
from misc import *

class fact(factic):
	"""
	an assertion of fact
	treated as a node which may be connected to other facts by rules
	"""
	subj = None
	verb = None
	obj = None
	
	# this is developing into a "facticity" interface
	#  facts should probably implement these as attributes, and rules as properties.
	veracity = True
	alpha = 0.0
	
	def __init__(self, **kwargs):
		"""
		Constructor:
		- Optionaly takes either a 'svo' tuple kwarg specifying subject, verb, object or 
			individual kwargs for each.
		- Optionally takes a 'veracity' kwarg to specify the implicit truth.
		"""
		
		if 'svo' in kwargs:
			self.subj, self.verb, self.obj = kwargs['svo']
		else:
			dict_to_attr(self, kwargs, ('subj','verb','obj'))
		
		dict_to_attr(self, kwargs, ('veracity','alpha'))