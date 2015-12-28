"""
permute:
    constructs a list with all valid permutations of any sequence
subset:
    constructs a list with all valid permutations of a specific length
combo:
    works like subset, but order doesn't matter: permutations of the same items are filtered out
"""

def permute(list):
    if not list:
        return [list]
    else:
        res = []
        for i in range(len(list)):
            """
            >>> res=[1,2,3,4,5]
            >>> res[:i] => [1, 2]
            >>> res[i+1:] => [4, 5]
            >>> res[i:i+1] => [3]
            """
            curRes = list[:i] + list[i+1:]
            for x in permute(curRes):
                res.append(list[i:i+1] + x)
        return res

def subset(list, size):
    if size == 0 or not list:
        return [list[:0]]
    else:
        result = []
        for i in range(len(list)):
            pick = list[i:i+1]
            rest = list[:i] + list[i+1:]
            for x in subset(rest, size - 1):
                result.append(pick + x)
        return result

def combo(list, size):
    if size == 0 or not list:
        return [list[:0]]
    else:
        result = []
        """
        >>> range(3) => [0, 1, 2]
        >>> range(0, 2) => [0, 1]
        """
        for i in range(0, (len(list) - size) + 1): # iff enough left
            pick = list[i:i+1]
            rest = list[i+1:] # drop [:i] part
            for x in combo(rest, size - 1):
                result.append(pick + x)
        return result