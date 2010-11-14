
class context:
	"""
	Context objects provide a view (in the MVC scheme) of a knowledge base (kb).
	
	The context is constructed by a query (call to a fact or rule) if
	one is not provided. Facts and rules are not directly aware of other
	facts and rules, relying on a context object instead.
	
	A context provides rete (ree-tee) lookups for rule evaluation.
	It also provides salience metadata to provide rule evaluation with
	optimized ordering of precedent (backchain) or dependent (forward
	chaining) evaluation.
	
	context objects act like dictionaries.
	"""
	__facts__ = {}
	__rules__ = {}
	def __init__():
		pass

class kb:
	"""
	kb is an abstract class. A kb implementation provides the data model
	for all knowledge upon which the expert system can operate.
	
	A KB is at its simplest, a naive hypercube of facts and rules. All
	rules and facts could with equal weight, possibly contribute to an
	evaluation. Traditionally, a rete improves on this by providing higher
	weighted network of links between rules and facts which effectively
	prunes the hypercube based on a boolean pattern match salience function.
	Also, a rete provides a cache of intermediate evaluation results to prevent
	the evaluation from happening twice on the same rule for efficiency and to
	prevent multiple evaluations of a rule from returning inconsistent values
	on subsequent evaluations.
	
	API:
		success = kb.assume(factOrRule)		# Adds a fact or a rule to the KB.
							## Might be a call to some other factory.
		factList = getFacts(factTemplate)	# Searches for facts matching a template
							## 3-tuple. Returns a list in unspecified order.
	"""
	__graph__ = {}
	"""
	The graph attribute is a dictionary of dictionaries. They keys are the target object and the values are a dictionary of
	metadata. Metadata may include neurons {netname: (target, weight)} or exploratory annotations.
	"""
	facts = {}
	rules = {}
	"""
	For testing purposes, a naive index is implemented. This will not scale well.
	The facts, rules attributes are dictionaries keyed on the facts' combinations.
	Given the facts:
		('Einstein','is','dead'),('Einstein','is','Albert Einstein')
	The facts index dict would explode into:
		{('Einstein','is','dead'):None,
		('Einstein','is',None):[('Einstein','is','dead'),('Einstein','is','Albert Einstein')],
		(None,'is','dead'):[('Einstein','is','dead'),],
		(None,'is','Albert Einstein'):[('Einstein','is','Albert Einstein'),]}
	"""
	def __init__():
		pass


class fact:
	"""
	A fact is essentially a tuple of subject, verb, object expressing simple
	declarative sentences.
	In a system of radical fallibility, each fact is subject to doubt, and
	may be questioned. Therefore, a fact may be called like a function to query
	it. 
	"""
	subject = None
	verb = None
	object = None
	id = (subject,verb,object)
	def __hash__(self):
		return self.id.__hash__()
	
	def __init__(self,*argv,**kwargs):
		if len(argv) == 3:
			self.subject, self.verb, self.object = argv
		else:
			if 'subject' in kwargs:
				self.subject = argv['subject']
			if 'verb' in kwargs:
				self.verb = argv['verb']
			if 'object' in kwargs:
				self.verb = argv['object']
	
	def __call__(self,context):
		# facts are identified by tuple
		if self.id in context:
			return True
		# rules are identified by dependent verb
		if self.verb in context:
			return context['verb'](self.subject,self.object)
		# default: None
		return None

class rule:
	"""
	If the precedents are all true, then so is the consequent.

	The key of the rule is the verb of the consequent.
	"""
	precedent = []
	consequent = None
	def __call__(self,*argv):
		"""
		Rules are the entry point for inferential work.
		A rule is called with context, subject, object.
		If the precedents are True, then the rule returns
		true.
		The arguments are a list of values for which
		logic clauses' terms will substitute when evaluated.
		
		given aRule:
			if (A,'is a',B) and (B,'is a',C) then (A,'is a',C)
		when evaluated with argv ('Fido','dog','mammal') will imply ('Fido','is a','mammal')
		
		Back chaining  does aRule('Fido','mammal') which then searches for salient facts and
			rules to satisfy the precedent conditions ('Fido','is a',B) and (B,'is a','mammal')
			This tests for the intersection on B. First pick one of the clauses, search for all
			possible factual values of B, then reduce that set to the intersection of all possible
			factual values of B from the other clause, then once all clauses are evaluated the
			remaining reduced facts prove the precedents therefore the consequent is asserted.
		
		The first step is a search for salient facts and rules, which is a map action, and the second
			is a reduce action. The evaluations in the reduce step might be recursive, so it is
			important to sort if possible from the cheapest to the most expensive. Where deep
			inferences might need to take place, several layers of rules might need to evaluate.
			
		"""
		
