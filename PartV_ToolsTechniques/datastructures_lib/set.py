"""
https://docs.python.org/2.4/lib/types-set.html
A set object is an unordered collection of immutable values.
    Common uses include membership testing,
    removing duplicates from a sequence,
    and computing mathematical operations such as intersection, union, difference, and symmetric difference.
    New in version 2.4.

Like other collections, sets support x in set, len(set), and for x in set.
Being an unordered collection, sets do not record element position or order of insertion.
Accordingly, sets do not support indexing, slicing, or other sequence-like behavior.

There are currently two builtin set types, set and frozenset.
    The set type is mutable -- the contents can be changed using methods like add() and remove().
        Since it is mutable, it has no hash value and cannot be used as either a dictionary key or as an element of another set.
    The frozenset type is immutable and hashable -- its contents cannot be altered after is created;
        however, it can be used as a dictionary key or as an element of another set.
"""

# Built-in set
def testBuiltinSet():
    x = set('abcde') # make set from an iterable/sequence
    y = {c for c in 'bdxyz'}
    print(x)
    print(y)

    print('e' in x) # memebership
    print(x - y) # difference
    print(x & y) # intersection
    print(x | y) # union

    z = set(['spam', 'ham', 'eggs']) # sequence of immutables
    print(z)
    # built-in set can't take mutable/unhashable type (here is list)
    # z = set(['spam', 'ham'], ['eggs', 'chicken'])
    # print(z)
    z = {'spam', 'ham', 'eggs'}
    print(z)
    z = set({'spam':[1, 1], 'ham': [2, 2], 'eggs':[3, 3]})
    print(z)

    s = {c.upper() * 4 for c in 'spamham'} # set comprehension
    print(s)
    s = list(set([1, 2, 3, 1, 2])) # remove duplicates
    print(s)

# Customized Set by using list
"""multi-instance, customizable, encapsulated set class"""
class Set:
    def __init__(self, value=[]):
        self.data = []
        self.concat(value)

    def intersect(self, other):
        res = []
        for x in self.data:
            if x in other:
                res.append(x)
        return Set(res)

    def union(self, other):
        res = self.data[:]
        for x in other:
            if not x in res:
                res.append(x)
        return Set(res)

    def concat(self, value):
        for x in value:
            if not x in self.data:
                self.data.append(x)

    def __len__(self): return len(self.data)
    def __getitem__(self, key): return self.data[key]
    def __and__(self, other): return self.intersect(other)
    def __or__(self, other): return self.union(other)
    def __repr__(self): return '<Set:' + repr(self.data) + '>'

def testSet(SetClass):
    users1 = SetClass(['Bob', 'Emily', 'Howard', 'Peeper'])
    users2 = SetClass(['Jerry', 'Howard', 'Carol'])
    users3 = SetClass(['Emily', 'Carol'])
    print(users1 & users2)
    print(users1 | users2)
    print(users1 | users2 & users3)
    print((users1 | users2) & users3)
    print(users1.data)

def testCustomizedSet():
    testSet(Set)

"""
For the previous Set class, the first problem you might encounter is:
    its performance: its nested for loops and in scans become exponentially slow.

Here use dictionary instead

Disadvantage: because dictionary keys must be immutable and values are stored in keys,
              dictionary sets can contain only things such as tuples, strings, numbers,
              and class objects with immutable signatures
    like built-in set, it can't take mutable/unhashable type (here is list)
    >>> set.Set([[1, 2],[3, 4]]) <Set:[[1, 2], [3, 4]]>
    >>> fastset.Set([[1, 2],[3, 4]])
    TypeError: unhashable type: 'list'
    >>> x = fastset.Set([(1, 2), (3, 4)])
    >>> x & fastset.Set([(3, 4), (1, 5)])
    <Set:[(3, 4)]>
"""
class SetOptimized(Set):
    def __init__(self, value=[]):
        self.data = {}
        self.concat(value)

    def intersect(self, other):
        res = {}
        for x in other:
            if x in self.data:
                res[x] = None
        return SetOptimized(res.keys())

    def union(self, other):
        res = {}
        for x in other:
            res[x] = None
        for x in self.data.keys():
            res[x] = None
        return SetOptimized(res.keys())

    def concat(self, value):
        for x in value:
            self.data[x] = None

    def __getitem__(self, index):
        return list(self.data.keys())[index]

    def __repr__(self):
        return '<SetOptimized:%r>' % list(self.data.keys())

def testSetOptimized():
    testSet(SetOptimized)


