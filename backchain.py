#
#  backchain.py
#  Monade
#
#  Created by Jeremy McMillan on 2/4/10.
#  Copyright (c) 2010 Jeremy McMillan. All rights reserved.
#
"""
Infers the truth of an assertion by resolving all of the precedent logic,
modus tollens

In contrast, a forwardchain infers all assertions affected by a given assertion,
modus ponens.

A back chaining inference asks if a given hypothetical fact is true.

fact0: Bob is child of Audrey
fact0.tuple = ('Bob','is child of','Audrey')
fact1: Cliff is child of Audrey
fact2: Bob is child of Nigel

rule0: if B is child of A and C is child of A, and B is not C, then B is sibling of C.
rule0.antecedent = and((B, "is child of", A),(C, "is child of", A))
rule0.consequent = (B, "is sibling of", C)
rule1: if A is sibling of B, then B is sibling of A.

Q: Is Cliff sibling of Bob?

The given facts introduce verb-clause "is child of", and the rules also introduce
verb-clause "is sibling of". To answer the question, we assume it is true, and test
the hypothesis against the available rules and facts. If there is a fact which
directly confirms or denies the hypothesis, we can return that boolean value.
If not, we must search for ways to infer that fact.

The hypotheis has the verb-clause "is sibling of" which we find in the consequent
of rule0. From rule0 we must append our hypothesis' case with the assumptions that
rule0 criteria are true, and test them as subordinate hypotheses. These are open
questions: "Cliff" "is child of" unknown, and "Bob" "is child of" unknown. First
we will attempt to infer these values by searching the knowledge base, but they may
be presented back to the user as questions if the proof cannot be concluded.

We generate two subset of facts which match either subject "Cliff" and  verb
"is child of" or subject "Bob" and verb "is child of". This enables us to build two
sets, one for "Cliff" and one for "Bob". Since all of the facts in each set have identical
elements 0 and 1, the sets need only contain the value of element 2

"""