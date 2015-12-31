"""
sort.py & reverse.py are serving an educational role,
built-in lists and functions generally accomplish
what we just did the hard way.
"""

def testBuiltInSort():
    """
    1, list object's sort method for arbitrary kinds of iterables,
        convert first if needed
    """
    temp1 = list("spam")
    temp1.sort()
    print(temp1)

    """
    2, sorted built-in function operates on any iterable
    so you don't need to convert, and returns a new sorted result list,
    it is not an in-place change, no side effects of changing the original list
    """
    temp2 = sorted("spam")
    print(temp2)

    """
    3, custom sorts
    """
    L = [{'n':3}, {'n':20}, {'n':0}, {'n':9}]
    L.sort(key=lambda x: x['n'])
    print(L)

def testBuiltinReverse():
    L = [2, 4, 1, 3, 5]
    L.reverse()
    print(L)

    L = [2, 4, 1, 3, 5]
    LL = list(reversed(L))
    print(L)
    print(LL)

