from datastructures_lib import set

# set.testBuiltinSet()
# set.testCustomizedSet()
# set.testSetOptimized()

import timer, sys

def setOperations(SetClass):
    set1 = SetClass(range(50)) # a 50-integer set
    set2 = SetClass(range(20))
    set3 = SetClass(range(10))
    set4 = SetClass(range(5))

    for i in range(5):
        interSet = set1 & set2 & set3 & set4 # 3 intersects
        unionSet = set1 | set2 | set3 | set4 # 3 unions

reps = int(sys.argv[1])
print('Set =>          ', timer.testWithTimer(reps, setOperations, set.Set))
print('SetOptimized => ', timer.testWithTimer(reps, setOperations, set.SetOptimized))

# python data_structures_set.py 50