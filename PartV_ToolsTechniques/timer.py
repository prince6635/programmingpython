import time

def testWithTimer(reps, func, *args):
   start = time.clock() # current CPU time in float seconds
   for i in range(reps):
       func(*args)
   return time.clock() - start