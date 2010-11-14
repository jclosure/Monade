#
#  kb.py
#  Monade
#
#  Created by Jeremy McMillan on 8/8/10.
#  Copyright (c) 2010 Jeremy McMillan. All rights reserved.
#
from Monade import *

class domain():
	"""
	A domain of expertise upon which Expert Systems inferences
	can be made and tested.
	
	facts is a dictionary of truth probability monads keyed by (subj, verb, obj) tuple
	rules is a dictionary of predicate logic relationship monads keyed by verb
	"""
	facts = {'s':{},'v':{},'o':{}}
	rules = {}
	def __init__(self,**kwargs):
		if 'facts' in kwargs: self.facts = kwargs['facts']
	
	def infer(self, premise):
		"""
		This recurses through the tree structure of self.facts + self.rules,
		and evaluates the argument.
		"""
		truth = premise(domain=self)
		yield truth
	
	def assert_facts(self, facts):
		"""
		Takes a dict as argument.
		The dict keys must be facts.
		The values must be boolean.
		"""
		for key in facts.keys():
			if len(key) == 3:
				# make a fact object and incorporate it.
				_fact = fact(svo=key, veracity=facts[key])
				s,v,o = key
				self.facts[(_fact.subject,_fact.verb,_fact.object)] = _fact
				# for each of s, v, o attributes index the fact
				for t,idx in ((s,self.facts['s']),(v,self.facts['v']),(o,self.facts['o'])):
					if t not in idx:
						idx[t] = []
					if _fact not in idx[t]:
						idx[t].append(_fact)
