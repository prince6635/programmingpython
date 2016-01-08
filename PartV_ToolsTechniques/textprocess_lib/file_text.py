# sum columns in a file
def sum(numCols, fileName):
    sums = [0] * numCols # [0]*3=>[0, 0, 0]
    for line in open(fileName):
        cols = line.split()
        for i in range(numCols):
            sums[i] += eval(cols[i])
    return sums

# sum with zips and comprehensions
def sumWithZipsAndListComprehensions(numCols, fileName):
    sums = [0] * numCols
    for line in open(fileName):
        cols = line.split(',')
        nums = [int(x) for x in cols]
        print('nums: ')
        print(nums)
        both = zip(sums, nums)
        print('both: ')
        print(both)
        sums = [x + y for (x, y) in both]
    return sums

# sum with dictionaries
def sumWithDictionaries(fileName):
    sums = {}
    for line in open(fileName):
        cols = [float(col) for col in line.split()]
        for pos, val in enumerate(cols):
            sums[pos] = sums.get(pos, 0.0) + val
    return sums