#!/usr/bin/env python2.3
#
#  test.py
#  Monade
#
#  Created by Jeremy McMillan on 7/29/10.
#  Copyright (c) 2010 Jeremy McMillan. All rights reserved.
#
"""
Story:
	Given a bunch of assumptions ( subject, verb-preposition, direct-object ) and
	some functions representing laws or rules of truth that produce additional 
	assertions ( subject, verb-preposition, direct-object )
	we wonder if a certain hypothetical fact is true...
	
	prob(0.5) && prob(0.25) = 0.5 * 0.25
	prob(0.5) || prob(0.25) = max(0.5, 0.25)
	
	hypothesis.infer(domain)
"""

def mk_test_kb():
	"""
	This makes the assertion:
	kb[('Bob', 'is-brother-of', 'Joe')] = True
	  but is really later transformed by bob's monad 'is-brother-of' into
	kb[('Bob','Joe')].assert('is-brother-of')
	"""
	kb = domain()
	kb.assert_facts({
			('Bob','is-brother-of','Joe'):True,
			('Bob','is-brother-of','Frank'):True,
			('Joe','is-father-of','Tom'):True
		})

	return kb

if __name__ == '__main__':
	# Take on the module's root as local namespace
	from pprint import PrettyPrinter
	pp = PrettyPrinter(indent=2)
	from Monade import *
	
	kb = mk_test_kb()
	"""
	  This makes the assertion:
	kb[('Bob', 'is-brother-of', 'Joe')] = True
	  but is really transformed by bob's monad 'is-brother-of' into
	kb[('Bob','Joe')].assert('is-brother-of')
	"""
	
	"""
      This tests the assertion:
	if kb['Bob']['is-brother-of']('Joe'): die()
	  which is orthogonal to
	kb[('Bob','Joe')].test('is-brother-of')
	  which is transformed into
	kb.test('Bob', 'is-brother-of', 'Joe')
	  which is actually implemented as a recursive evaluation and search
	kb.infer(('Bob', 'is-brother-of', 'Joe'))
	"""
	
	# hypothesis:
	#   Frank is-uncle-of Tom