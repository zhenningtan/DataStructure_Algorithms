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

def QuickSort(arr):
    ''' return a sorted array '''
    n = len(arr)
    if n <= 1:
        return arr
    else:
        p = ChoosePivot(arr)  # choose a pivot, move it to the first element
        #print "pivot is", p
        ind = arr.index(p)
        if ind != 0:
            arr[0], arr[ind] = arr[ind], arr[0]
        arr = Partition(arr)
        inds = arr.index(p)
        arr[0:inds] = QuickSort(arr[0:inds])
        if inds < n-1:
            arr[(inds +1):n] = QuickSort(arr[(inds +1):n])
        return arr

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
    #print "after partition:", arr
    #print ""
    return arr

test = [9, 4, 3, 2, 1, 8, 6, 5, 7,10, 12, 15, 11]
print "original", test
print ""
print QuickSort(test)
