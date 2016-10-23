
def parent(i):
    '''get the parent position for element i in heap A'''
    p = (i+1)/2 -1
    return p

# max-heap operations
def heap_increase_key(A, i, key):
    ''' increase a key at position i in max-heap'''
    if key < A[i]:
        print "error: new key is smaller than current key"
    A[i] = key
    while i > 0 and A[parent(i)] < A[i]:
        A[parent(i)], A[i] = A[i], A[parent(i)]
        i = parent(i)
    return A

def max_heap_insert(A, key):
    '''insert a key in a max-heap'''
    size = len(A) +1
    A.append(float("-inf"))
    return heap_increase_key(A, size-1, key)

def max_heapify(A, i):
    '''build max-heap at position i'''
    l = 2*i + 1  # left child
    r = 2*i + 2  # right child

    if l < len(A) and A[i] < A[l]:
        largest = l
    else: largest = i

    if r < len(A) and A[r] > A[largest]:
        largest =r

    if largest != i :
        A[largest], A[i] = A[i], A[largest]

        A = max_heapify(A, largest)
    return A

def heap_extract_max(A):
    '''extract the max in max-heap'''
    A[0] = A[-1]
    size = len(A) -1
    return max_heapify(A[0:size], 0)

# min-heap operations
def heap_decrease_key(A, i, key):
    ''' decrease a key at position i in min-heap'''
    if key > A[i]:
        print "error: new key is larger than current key"
    A[i] = key
    while i > 0 and A[parent(i)] > A[i]:
        A[parent(i)], A[i] = A[i], A[parent(i)]
        i = parent(i)
    return A

def min_heap_insert(A, key):
    '''insert a key in a min-heap'''
    size = len(A) +1
    A.append(float("inf"))
    return heap_decrease_key(A, size-1, key)

def min_heapify(A, i):
    '''build min-heap at position i'''
    l = 2*i + 1  # left child
    r = 2*i + 2  # right child
    if l < len(A) and A[i] > A[l]:
        smallest = l
    else: smallest = i
    if r < len(A) and A[r] < A[smallest]:
        smallest = r
    if smallest != i :
        A[smallest], A[i] = A[i], A[smallest]
        A = min_heapify(A, smallest)
    return A


def heap_extract_min(A):
    '''extract the min in min-heap'''
    A[0] = A[-1]
    size = len(A) -1
    return min_heapify(A[:size], 0)


# divid input stream of numbers to two heaps
# low is a max-heap structure
# high is a min-heap structure
# median is within max(low) and min(high)
def median_maintenence(array):
    '''consider the array as a stream, find the median when add
    elements to the array'''
    low = [] # max-heap for left part numbers
    high = [] # min-heap for right part numbers
    i = 0
    j = 0

    if array[0] <= array[1]:
        low = max_heap_insert(low, array[0])
        i +=1
        high = min_heap_insert(high, array[1])
        j +=1
    else:
        low = max_heap_insert(low, array[1])
        i +=1
        high = min_heap_insert(high, array[0])
        j +=1

    # add median for the first two streams
    median_list = [array[0], low[0]]
    median = low[0]

    for k in array[2:]:
        # add k to low or high heap
        if k <= median:
            low = max_heap_insert(low, k)
            i += 1
        else:
            high = min_heap_insert(high, k)
            j +=1

        # if two heaps differ by more than one element
        # extract the root and add to the other heap
        if (i - j) > 1:
            extract = low[0]
            low = heap_extract_max(low)
            i -=1
            high = min_heap_insert(high, extract)
            j +=1
        if (j -i) > 1:
            extract = high[0]
            high = heap_extract_min(high)
            j -=1
            low = max_heap_insert(low, extract)
            i += 1

        # median is within the root node of two heaps
        if i >= j:
            median = low[0]
        else:
            median = high[0]
        if i%1000 ==0: # to track the process of calculation 
            print "median for %s iteration is %s" %(i,median)
        median_list.append(median)

    return sum(median_list)%len(array)

test1 = [9, 9, 7, 1, 2,3,4,5,6,7,8,9]
test = [2,8,9,7,3,1,4]


# read in data
def readData(file):
    array = []
    with open(file, "r") as f:
        for line in f:
            elem = line.strip()
            if elem:
                array.append(int(elem))
    return array

data = readData("Median.txt")
print "length:", len(data)


import time
start = time.time()
print "calculate median ..."
print median_maintenence(data)
end = time.time()
print "time eclipsed:", (end-start), "seconds"
