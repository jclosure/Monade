#
#  rule.py
#  Monade
#
#  Created by Jeremy McMillan on 2/7/10.
#  Copyright (c) 2010 Jeremy McMillan. All rights reserved.
#
"""
A rule defines a unit of predicate logic. It takes the basic form of IF ==> THEN.

It has a consequent as an attribute, and it has a list of conditions. It attempts
to assert the consequent as a fact if the premise is true. 
The consequent is a facts.fact, and the premise may be a set of premises.
If the premise is a set of disjoint attribute is True, then 
attribute is true, then the 
"""
import itertools
from monad import factic

class case(set):
	"""
	A case is a set of facts.
	It implements a form() method, which is identical to that of any congruent case.
	A premise of a rule is a formula, and it is identical to the form of
		any case which fits the model.	
	"""
	__verbs__ = tuple()
	__terms__ = tuple()
	__subjects__ = tuple()
	__objects__ = tuple()
	terms = [] # make case.terms an immutable property or something
	
	def __init__(self,*args):
		verbs = []
		subjs = []
		objs = []
		terms = []
		# need to factor this loop out in order to make case.terms a property
		for f in args:
			verb = f.verb[:]
			subj = f.subj[:]
			obj = f.obj[:]
			if verb not in verbs:
				verbs.append(verb)
			if subj not in subjs:
				subjs.append(subj)
				terms.append(subj)
			if obj not in objs:
				objs.append(obj)
				terms.append(obj)
			self.add(f)
		self.__verbs__ = tuple(verbs)
		self.__subjects__ = tuple(subjs)
		self.__objects__ = tuple(objs)
		self.__terms__ = tuple(terms)
	
	@property
	def verbs(self):
		"""
		tuple of verbs in the case facts
		"""
		return self.__verbs__
	
	@property
	def terms(self):
		"""
		"""
		return self.__terms__
	
	@property
	def form(self):
		"""
		The formula of a case.
		"""
		terms = self.terms
		return [(terms.index(x.subj), verb, terms.index(x.obj)) for x in self]

class premise(case):
	"""
	Implements the hypothetical case forming the premise of a rule.
	"""
	
	def _and_(a,b):
		"""
		logical conjunction
		"""
		return a and b
	
	def _or_(a,b):
		"""
		logical inclusive disjunction
		"""
		return a or b

	def _xor_(a,b):
		"""
		logical exclusive disjunction
		"""
		return a and not b or not a and b
		
	# TODO: lambda to bench a combination of conditions from a generator
	# trials = reduce(_and_, ())
	
	# yield reduce(_or_, trials)
		

class rule(factic):
	"""
	an assertion of predicate logic:
	if P then Q.
	
	Attributes:
		P is a list of predicate conditions under which the rule will assert Q as a fact.
		Q is a consequent(fact), enforced conditionally if predicte list P is true.
		disjoint is a boolean causing P to reduce by logical XOR if True or by logical AND
			if False.
	
	A rule "fires" when a question call it as a function. 
	The calling question is associable to all rules with matching consequent verb.
	The question calls the rule with subject and object, and context as arguments.
	The rule first maps the arguments supplied by the question to instantiate 
		the questions for each of the premises.
	"""
	P = premise()
	Q = None
	disjoint = False
	# __terms__ are positional arguments to Nulls in P's conditions
	#	Evaluating a rule asks its context kb to provide a list of the combinations of facts
	#	matching the non-Nulls in P's conditions. Those combinations are then mapped to
	#	__terms__ and reduced by boolean logic to determine whether or not Q is consequential.
	__terms__ = []
	def __set_P__(self, premises):
		self.P = [fact(svo=key, veracity=premises[key]) for key in premises.keys()]
	
	def __set_Q__(self, consequent):
		self.Q = fact(svo=consequent.keys()[0], veracity=consequent[consequent.keys(0)])
	
	def __init__(self, P, Q, **kwargs):
		"""
		Takes a dictionary of facts
		"""
		self.__set_P__(P)
		self.__set_Q__(Q)
	
	def __bench__(self,considerations):
		"""
		Bench test some facts [(lvalue, verb, rvalue), ...] against the premise
		"""
		# vectors is the cartesian product of all possible sets of facts which 
		#   have matching forms
		vectors = [apply(itertools.product,[considerations[verb] for verb in self.verbs])]
		# after vectors is built up, those vectors which aren't congruent with the whole
		#   premise are filtered out, and the salient ones are returned.
		#### iterate through the terms of the premise or consideration 
		####    and append the new ones to a termlist
		#### Then reduce the premise/consideration to a list of the indexes of termlist
		####    to get the platonic form of the premise or consideration
		#### Return a vector of the considerations with an equivalent platonic form to that of
		####    the premise
		#### The 
		return considerations
	
	def __assert__(self,trial):
		"""
		Map a consideration into the premise by terms and return a boolean indicating
		 whether it matches.
		trial = (('Bob','Joe'),('Joe','Tom'))
		benchmark = (('A','B'),('B','C'))
		terms = {'A':['Bob'],'B':['Joe','Joe'],'C':'Tom')
		"""
		if self.premise.form = trial.form:
			return True
		else:
			return False
	
	def fchain(case):
		"""
		Takes a case (for best results sorted in order of decreasing salience) and
		  returns facts which may be asserted by the rule in the given case.
		  This is essentially a search of the context for rules and all complimentary facts.
		  It does NOT actually assert the resulting facts in the context/kb.
		Return values:
			True (the premise is True)
			False (the premise is not true)
			None (the vector does not cover the premise)
		
		Iterates over facts in vector, one for each self.verb, and
		  returns a boolean indicating whether the vector satisfies
		  the premise.
		Given vector =
		  facts = {
			('Bob','is-brother-of','Joe'):True,
			('Bob','is-brother-of','Frank'):True,
			('Joe','is-father-of','Tom'):True
		  }
		  
		  rules = {
		    (('A','is-brother-of','B'),
			('B','is-father-of','C')) : ('A','is-uncle-of','C')
		    }
		"""
		# Assume the premise is false therefore no inferences
		result = False
		# Make a dict, considerations, of the given facts keyed by each of their verbs.
		# Consider only those facts which have matching verb in self.verbs
		considerations = dict([(k,[(v[0],v[2]) for v in case.keys() if v[1] == k]) for k in self.verbs])
	
	def __call__(self, context, *args):
		"""
		Fire the rule.
		"""
		# This is where Monads make sense..
		if 'context' not in kwargs:
			kwargs['context'] = None
		try:
			val = self.P(context=kwargs['context'])
		except TypeError:
			if self.disjoint:
				"""
				Test the set of premises as a disjunction (logical xor)
				Boolean: exactly one of the set must be true, else the expression is false
				"""
				pass
			else:
				"""
				Test the set of premises as a conjuntion (logical and)
				Boolean: map/reduce
				"""
				pass