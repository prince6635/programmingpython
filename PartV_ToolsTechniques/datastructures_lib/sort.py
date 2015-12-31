def sort(list, field):
    res = []
    for x in list:
        i = 0
        for y in res:
            if x[field] <= y[field]:
                break
            i += 1
        res[i:i] = [x]
    return res

def sort_generic(sequence, func=(lambda x,y: x <= y)):
    res = sequence[:0]
    for j in range(len(sequence)):
        i = 0
        for y in res:
            if func(sequence[j], y):
                break
            i += 1
        res = res[:i] + sequence[j:j+1] + res[i:]
    return res

def testSort():
    table = [{'name':'john', 'age':25}, {'name':'doe', 'age':32}]
    print(sort(table, 'name'))
    print(sort(table, 'age'))
    table = [('john', 25), ('doe', 32)]
    print(sort(table, 0))
    print(sort(table, 1))


def testSortGeneric():
    table = ({'name': 'doe'}, {'name': 'john'})
    print(sort(list(table), (lambda x, y: x['name'] > y['name'])))
    print(sort(tuple(table), (lambda x, y: x['name'] <= y['name'])))
    print(sort('xybaz'))
