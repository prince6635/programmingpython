from __future__ import print_function # enable the Python 3 syntax if you are using Python 2.6 or 2.7

from datastructures_lib import stack

# stack.testStack()
# stack.testStackWithLog()
# stack.testOptimizedStack()
# stack.testStackFinal()

reps = 200
from timer import testWithTimer
from sys import argv
pushes, pops, items = (int(arg) for arg in argv[1:])

def stackOperations(stackClass):
    x = stackClass('spam') # make a stack object
    for i in range(pushes):
        x.push(i)
    for i in range(items):
        t = x[i]
    for i in range(pops):
        x.pop()

for mod in (stack.Stack, stack.StackOptimized, stack.StackFinal):
    print('%s: ' % mod.__name__, end=' ')
    print(testWithTimer(reps, stackOperations, mod))

# python data_structures.py 200 200 200
# python data_structures.py 200 50 200
# python data_structures.py 200 200 50
# python data_structures.py 200 200 0
"""
The results show that the tuple-based stack (stack3) performs better
when we do more pushing and popping, but worse if we do much indexing.

The in-place change stacks (stack4) are almost always fastest,
unless no indexing is done at all-tuples (stack3) win by a hair in the last test case.
"""

