def parent(pos): 
    return pos // 2
  
def leftChild(pos): 
    return 2 * pos

def rightChild(pos): 
    return 2 * pos + 1

def isLeaf(lst, pos): 
    size = len(lst)
    if pos >= size // 2 and pos <= size: 
        return True
    return False

def swap(lst, pos1, pos2):
    lst[pos1], lst[pos2] = lst[pos2], lst[pos1]

def maxHeapify(lst, pos): 
    if not isLeaf(lst, pos): 
        if lst[pos] < lst[leftChild(pos)] or lst[pos] < lst[rightChild(pos)]: 
            if lst[leftChild(pos)] > lst[rightChild(pos)]: 
                swap(lst, pos, leftChild(pos)) 
                maxHeapify(lst, leftChild(pos)) 
            else: 
                swap(lst, pos, rightChild(pos)) 
                maxHeapify(lst, rightChild(pos)) 

def buildHeap(lst):
    for pos in range(len(lst) // 2, -1, -1):
        maxHeapify(lst, pos)

def insert(lst, elt): 
    lst.append(elt)
    current = len(lst) - 1
    while lst[current] > lst[parent(current)]: 
        swap(lst, current, parent(current)) 
        current = parent(current) 

def extractMax(lst): 
    mx = lst[0]
    last = len(lst) - 1
    lst[0] = lst[last]
    del lst[last]
    maxHeapify(lst, 0)
    return mx