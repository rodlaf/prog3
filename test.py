from random import randint
from time import time
from partition import *
NUMTRIALS = 100
NUMINTS = 100
NUMDIGITS = 12

A = []

def newNumbers():
    for _ in range(NUMINTS):
        A.append(randint(1, 10 ** NUMDIGITS))

def printResult(result):
    print('Trial: '+str(result[0])+'   Algorithm: '+str(result[1])+'   Residue: '+str(result[2])+'   Time: '+str(result[3]))

results = []
for trial in range(1, NUMTRIALS + 1):
    newNumbers()
    
    start = time()
    residue = KK(A)
    end = time()
    result = (trial, 'KK', residue, end - start)
    results.append(result)
    printResult(result)

    start = time()
    residue = repeatedRandom(A)
    end = time()
    result = (trial, 'Repeated Random', residue, end - start)
    results.append(result)
    printResult(result)

    start = time()
    residue = hillClimbing(A)
    end = time()
    result = (trial, 'Hill Climbing', residue, end - start)
    results.append(result)
    printResult(result)

    start = time()
    residue = simulatedAnnealing(A)
    end = time()
    result = (trial, 'Simulated Annealing', residue, end - start)
    results.append(result)
    printResult(result)

    start = time()
    residue = prepartitionedRepeatedRandom(A)
    end = time()
    result = (trial, 'Prepartitioned Repeated Random', residue, end - start)
    results.append(result)
    printResult(result)

    start = time()
    residue = prepartitionedHillClimbing(A)
    end = time()
    result = (trial, 'Prepartitioned Hill Climbing', residue, end - start)
    results.append(result)
    printResult(result)

    start = time()
    residue = prepartitionedSimulatedAnnealing(A)
    end = time()
    result = (trial, 'Prepartitioned Simulated Annealing', residue, end - start)
    results.append(result)
    printResult(result)


f=open('result.txt','w')
for elt in results:
    f.write(str(elt)+'\n')
f.close()

    

