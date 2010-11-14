#
#  monad.py
#  Monade
#
#  Created by Jeremy McMillan on 2/4/10.
#  Copyright (c) 2010 Jeremy McMillan. All rights reserved.
#

# Ideas:
#  Each rule/fact in a knowledge base is callable, to test itself.
#    Everything can be questioned!
#    Querying the expert system is actually invocation of the fact factory.
#  Objects in the knowledge base know how to search for their precedents/antecedents.
#    The result of a search is a rete network.
#    Precedents/antecedents can be redundant, and may have confidence vectors.
#    Objects can store metadata about their rete neighborhood.
#      rete neighborhood can be a vector of tuples (neighbor, confidence) for n degrees of separation
#    Objects can notify their rete neighbors of confidence, and effect a publish/subscribe model
#      for rete participation.
#  
# import zope.interface

class Monad(type):
	"""
	A monad "binds" which takes an expression and returns a 
		function in which 
	a mondad returns
			the evaluation of the bound expression.

	We're going to use a metaclass to "bind" which will
	give us a class (implementing __call__ which makes it a function)
	which returns the evaluation of the target expression.
	
	When we traverse a rete network, we make decisions about salience.
	When we know the salience relationships, they can be "wired" together
	  as a tree of function calls which call their precedents. Rather than
	  simply calling the functions, this mechanism allows us to persist the
	  calling structure to implement a proof.
	
	The big experiment:  
	Monad'ing an object will take an object, interface tuple,
	  and return a monad-ized object, which is a callable function, implementing
	  the interface specified.
	"""
	def __new__(meta, classname, bases, classDict):
		return type.__new__(meta, classname, bases, classDict)
	
	def __call__(self, *args, **kwargs):
		return notImplementedError




class factic():
	"""
	An abstract base class to provide common interface features for callable objects
	  intended to assert facts in a KB domain.
	"""
	context = None
	
	def __init__(self, *args, **kwargs):
		"""
		Any attribute listed in self.__arg_attrs__ may be specified in
		  **kwargs
		"""
		for kwarg in self.__arg_attrs__:
			if kwarg in self.__class__.__dict__:
				self.__class__.__dict__[kwarg] = args[kwarg]
	
	def __call__(self,**kwargs):
		"""
		KB factic objects are callable. Calling a fact or rule, for example, "interrogates"
		  the object, given as an argument a context object which implements an infer method.
		By default, calling a factic object is a proxy for context.infer(factic_object).
		"""
		if 'context' in kwargs:
			context = kwargs['context']
		else:
			context = domain()
		return context.infer(self)
	
	from misc import dict_to_attr
