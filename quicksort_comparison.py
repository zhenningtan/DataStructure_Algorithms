# quick sort

def ChoosePivot(arr):
    return arr[0]  # pick the first element
    #return arr[-1] # pick the last element
    #return median([arr[0], arr[-1], arr[len(arr)/2]])

def Partition(arr):
    i = 1
    for j in range(1, len(arr)):
        if arr[j] < arr[0]:
            arr[i], arr[j] = arr[j], arr[i]
            i +=1

        j +=1
    arr[0], arr[i-1] = arr[i-1], arr[0]

def QuickSort(arr, comparison = 0):
    ''' return a sorted array '''
    n = len(arr)
    if n <= 1:
        return arr, comparison
    else:
        comparison += (n-1)
        p = ChoosePivot(arr)  # choose a pivot, move it to the first element
        #print "pivot is", p
        ind = arr.index(p)
        if ind != 0:
            arr[0], arr[ind] = arr[ind], arr[0]
        arr = Partition(arr)
        inds = arr.index(p)
        arr[0:inds], comparison = QuickSort(arr[0:inds], comparison)
        if inds < n-1:
            arr[(inds +1):n], comparison = QuickSort(arr[(inds +1):n], comparison)
        return arr, comparison

def ChoosePivot(arr):
    #return arr[0]  # pick the first element
    #return arr[-1] # pick the last element
    return sorted([arr[0], arr[-1], arr[len(arr)/2-1 + len(arr)%2]])[1]

def Partition(arr):
    i = 1
    for j in range(1, len(arr)):
        if arr[j] < arr[0]:
            arr[i], arr[j] = arr[j], arr[i]
            i +=1
        j +=1
    arr[0], arr[i-1] = arr[i-1], arr[0]
    #print "after partition:", arr
    #print ""
    return arr

'''

test = [3, 2, 1]
print "original", test
print "sorted:", QuickSort(test)

'''

comparison = 0
array = []
with open("QuickSort.txt", "r") as f:
    for line in f:
        array.append(int(line.strip()))

result  = QuickSort(array)

print "comparison:", result[1]
print "length of array:", len(array)
print "first few elemnts of sorted array:", result[0][1:10]
