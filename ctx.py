#
#  ctx.py
#  Monade
#
#  Created by Jeremy McMillan on 11/14/10.
#  Copyright (c) 2010 Jeremy McMillan. All rights reserved.
#
#
class ctx():
	"""
	ctx is an abstract context in which facts and rules may relate to each other.
	
	ctx is the base class for both kb and proof classes and implements the basic
		graph functionality to map ephemeral (stateless) or persistent (stored)
		relationships, but does not implement any storage.
	"""

class proof(ctx):
	"""
	A proof is an ephemeral context which has a head node and can be used as a boolean.
	
	Where a ctx is a graph asserting all possible relationships between facts and rules,
		a proof is a directed graph (digraph) or tree derived by searching a ctx for
		salient rules and facts.
	"""