def reverse(list):
    # if list == []:
    # won't work at all for nonlists
    if not list:
        return list
    else:
        return reverse(list[1:]) + list[:1]

def iterate_reverse(list):
    res = list[:0]
    for i in range(len(list)):
        res = list[i:i+1] + res
    return res

def testReverse():
    print(reverse([1, 2, 3]))
    print(iterate_reverse([1, 2, 3]))
    print(reverse("spam"))
    print(iterate_reverse("spam"))
