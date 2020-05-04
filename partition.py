from random import choice, randint, random
from maxheap import buildHeap, extractMax, insert
from math import exp

MAX_ITER = 25000

def KK(A):
    H = A.copy()
    buildHeap(H)
    while len(H) > 1:
        x = extractMax(H)
        y = extractMax(H)
        insert(H, x - y)
    return H[0]

def randomSolution(len):
    S = []
    for _ in range(len):
        S.append(choice([-1, 1]))
    return S

def residue(A, S):
    return abs(sum([sign * num for sign, num in zip(S, A)]))

def randomNeighbor(S):
    nbor = S.copy()
    i = randint(0, len(S) - 1)
    j = randint(0, len(S) - 1)
    while i == j:
        j = randint(0, len(S) - 1)
    nbor[i] = -nbor[i]
    if choice([True, False]):
        nbor[j] = -nbor[j]
    return nbor

def repeatedRandom(A):
    S = randomSolution(len(A))
    for _ in range(MAX_ITER):
        new_S = randomSolution(len(A))
        if residue(A, new_S) < residue(A, S):
            S = new_S
    return residue(A, S)

def hillClimbing(A):
    S = randomSolution(len(A))
    for _ in range(MAX_ITER):
        new_S = randomNeighbor(S)
        if residue(A, new_S) < residue(A, S):
            S = new_S
    return residue(A, S)

def T(i):
    return (10 ** 10) * (0.8 ** (i // 300))

def simulatedAnnealing(A):
    S_1 = randomSolution(len(A))
    S_3 = S_1
    for i in range(MAX_ITER):
        S_2 = randomNeighbor(S_1)
        R_1 = residue(A, S_1)
        R_2 = residue(A, S_2)
        R_3 = R_1
        if R_2 < R_1:
            S_1 = S_2
            R_1 = R_2
        elif random() < exp(-(R_2 - R_1) / T(i)):
            S_1 = S_2
            R_1 = R_2
        if R_1 < R_3:
            S_3 = S_1
            R_3 = R_1
    return R_3

def randomPartition(len):
    P = []
    for _ in range(len):
        P.append(randint(0, len - 1))
    return P

def randomNeighborPartition(P):
    nbor = P.copy()
    i = randint(0, len(nbor) - 1)
    j = randint(0, len(nbor) - 1)
    while nbor[i] == j:
        j = randint(0, len(nbor) - 1)
    nbor[i] = j
    return nbor

def partitionResidue(A, P):
    new_A = [0] * len(A)
    for j in range(len(A)):
        new_A[P[j]] += A[j]
    return KK(new_A)

def prepartitionedRepeatedRandom(A):
    P = randomPartition(len(A))
    for _ in range(MAX_ITER):
        new_P = randomPartition(len(A))
        if partitionResidue(A, new_P) < partitionResidue(A, P):
            P = new_P
    return partitionResidue(A, P)

def prepartitionedHillClimbing(A):
    P = randomPartition(len(A))
    for _ in range(MAX_ITER):
        new_P = randomNeighborPartition(P)
        if partitionResidue(A, new_P) < partitionResidue(A, P):
            P = new_P
    return partitionResidue(A, P)

def prepartitionedSimulatedAnnealing(A):
    P_1 = randomPartition(len(A))
    P_3 = P_1
    for i in range(MAX_ITER):
        P_2 = randomNeighborPartition(P_1)
        R_1 = partitionResidue(A, P_1)
        R_2 = partitionResidue(A, P_2)
        R_3 = R_1
        if R_2 < R_1:
            P_1 = P_2
            R_1 = R_2
        elif random() < exp(-(R_2 - R_1) / T(i)):
            P_1 = P_2
            R_1 = R_2
        if R_1 < R_3:
            P_3 = P_1
            R_3 = R_1
    return R_3

# Driver code
# from sys import argv

# with open(argv[3], 'r') as f:
#     A = [int(line) for line in f]

# code = int(argv[2])

# if code == 0:
#     print(KK(A))

# elif code == 1:
#     print(repeatedRandom(A))

# elif code == 2:
#     print(hillClimbing(A))

# elif code == 3:
#     print(simulatedAnnealing(A))

# elif code == 11:
#     print(prepartitionedRepeatedRandom(A))

# elif code == 12:
#     print(prepartitionedHillClimbing(A))

# elif code == 13:
#     print(prepartitionedSimulatedAnnealing(A))