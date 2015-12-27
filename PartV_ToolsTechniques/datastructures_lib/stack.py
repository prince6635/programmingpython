from __future__ import print_function # enable the Python 3 syntax if you are using Python 2.6 or 2.7

# list is often adequate for implementing a stack
# because we can add and delete items from either the beginning (left) or the end (right)

class error(Exception): pass

# top is front-of-list
class Stack:
    def __init__(self, start=[]):
        self.stack = []
        for x in start:
            self.push(x)
        self.reverse()

    def push(self, obj):
        self.stack = [obj] + self.stack

    def pop(self):
        if not self.stack:
            raise error('underflow')

        # see the below example for *
        # top, *self.stack = self.stack # pythone 3
        top, self.stack = self.stack[0], self.stack[1:] # python 2
        return top

    def top(self):
        if not self.stack:
            raise error('underflow')

        return self.stack[0]

    def empty(self):
        return not self.stack

    # overloads
    # print, repr(),..
    def __repr__(self):
        return '[Stack:%s]' % self.stack

    # '==', '!='?
    def __eq__(self, other):
        return self.stack == other.stack

    # len(instance), not instance
    def __len__(self):
        return len(self.stack)

    # instance1 + instance2
    def __add__(self, other):
        return Stack(self.stack + other.stack)

    # instance * reps
    def __mul__(self, reps):
        return Stack(self.stack * reps)

    # see also __iter__
    # instance[i], [i:j], in, for
    def __getitem__(self, offset):
        return self.stack[offset]

    # instance.sort()/reverse()/..
    def __getattr__(self, name):
        return getattr(self.stack, name)


"""
import random

def arbitrary():
    return [x for x in range(1, random.randint(3,10))]

a, b, *rest = arbitrary()

# a = 1
# b = 2
# rest = [3,4,5]
"""

"""
Customization: Performance Monitors
customize stack for usage data
"""
class StackWithLog(Stack):
    pushes = pops = 0

    def __init__(self, start=[]):
        self.maxlen = 0
        Stack.__init__(self, start)

    def push(self, obj):
        Stack.push(self, obj)
        StackWithLog.pushes += 1
        self.maxlen = max(self.maxlen, len(self))

    def pop(self):
        StackWithLog.pops += 1
        return Stack.pop(self)

    def stats(self):
        return self.maxlen, self.pushes, self.pops

"""
In Stack, both operations make copies of the wrapped list object.
For large stacks, this practice can add a significant time penalty.

Here we can store the stacked objects in a binary tree of tuples:
each item may be recorded as a pair, (object, tree),
where object is the stacked item and tree is either another tuple pair
giving the rest of the stack or None to designate an empty stack.
A stack of items [1,2,3,4] would be internally stored as a tuple tree
(1,(2,(3, (4,None)))).
"""
class StackOptimized:
    def __init__(self, start=[]):
        self.stack = None
        for i in range(-len(start), 0):
            self.push(start[-i - 1])

    def push(self, node):
        # new root tuple: (node, tree)
        self.stack = node, self.stack

    def pop(self):
        node, self.stack = self.stack
        return node

    def empty(self):
        return not self.stack

    # on: len, not
    def __len__(self):
        len, tree = 0, self.stack
        while tree:
            len, tree = len+1, tree[1]
        return len

    # on: x[i], in, for
    def __getitem__(self, index):
        len, tree = 0, self.stack
        while len < index and tree:
            len, tree = len+1, tree[1]
        if tree:
            return tree[0]
        else:
            raise IndexError()

    def __repr__(self):
        return '[FastStack:' + repr(self.stack) + ']'

"""
!!!The one should use when write code!!!
top is end-of-list:
optimize with in-place list operations
"""
class StackFinal:
    def __init__(self, start=[]):
        self.stack = []
        for x in start:
            self.push(x)

    def push(self, obj):
        self.stack.append(obj) # top is end-of-list

    def pop(self):
        if not self.stack:
            raise error('underflow')
        return self.stack.pop() # like fetch and delete stack[-1]

    def top(self):
        if not self.stack:
            raise error('underflow')
        return self.stack[-1]

    def empty(self):
        return not self.stack

    def __len__(self):
        return len(self.stack)

    def __getitem__(self, offset):
        return self.stack[offset]

    def __repr__(self):
        return '[Stack:%s]' % self.stack

def testStack():
    s1 = Stack()
    s1.push('spam')
    s1.push(123)
    print(s1)

    s2 = Stack()
    s2.push(3.1415)
    s2.push(s1.pop())
    print(s1, s2)

    s3 = Stack()
    for c in 'spam':
        s3.push(c)
    while s3:
        print(s3.pop(), end=' ')

    s3 = s1 + s2
    print(s3)
    for item in s3:
        print(item, end=' ')

    s3.reverse()
    print(s3)

def testStackWithLog():
    x = StackWithLog()
    y = StackWithLog()
    for i in range(3):
        x.push(i)
    for c in 'spam':
        y.push(c)

    print(x, y)
    print(x.stats())
    print(y.stats())
    x.pop()
    y.pop()
    print(x.stats())
    print(y.stats())

def testOptimizedStack():
    x = StackOptimized()
    y = StackOptimized()
    for c in 'spam':
        x.push(c)
    for i in range(3):
        y.push(i)

    print(x, y)
    print(len(x), ', ', x[2], ', ', x[-1])
    x.pop()
    print(x)
    while y:
        print(y.pop(), end=' ')

def testStackFinal():
    x = StackFinal()
    y = StackFinal()
    x.push('spam')
    x.push(123)
    print(x)

    y.push(3.1415)
    y.push(x.pop())
    print(x, y)
    print(y.top())
