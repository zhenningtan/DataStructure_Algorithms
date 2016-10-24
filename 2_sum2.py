import time
def readData(file):
    array=[]
    with open(file, "r") as f:
        for line in f:
            elem = line.strip()
            if elem:
                num = int(elem)
                array.append(num)
    return array

array = readData("prob-2sum.txt")
print len(array)
print min(array), max(array)


#==============================
# sort the array in merge sort
def merge(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)

    n = n1 + n2
    marray = [0] * n

    k = 0
    i = 0
    j = 0
    #compare arr1 and arr2 and add the smaller number to the sorted array
    while i < n1 and j < n2:
        if arr1[i] <= arr2[j]:
            marray[k] = arr1[i]
            i +=1
        else:
            marray[k] = arr2[j]
            j +=1
        k +=1
    # add the remaining elements of arr1 or arr2 to the sorted array if any
    while i < n1:
        marray[k] = arr1[i]
        i+=1
        k+=1
    while j < n2:
        marray[k] = arr2[j]
        j+=1
        k+=1
    return marray


def mergeSort(arr):
    n = len(arr)
    if n <=1:
        return arr
    else:
        left = mergeSort(arr[0:n/2])
        right = mergeSort(arr[n/2:n])
        merged = merge(left, right)
        return merged
#=========================


start = time.time()
array = mergeSort(array)
end = time.time()
print "array sorted"
print "time eclipsed:", (end-start), "seconds"

print "first element:", array[0]
print "last element:", array[-1]

#======================
# for each t value, go from both ends of a sorted array
# to make the sum approaching t. running time is O(n)
def two_sum(array, t):
    low = 0
    high = len(array)-1
    found = False
    while low < high and not found:
        sum = array[low] + array[high]
        if sum == t:
            found = True
        elif sum > t: # if sum > t, decrease the big number
            high -=1
        else: # if sum <t, increase the lower number
            low +=1
    return found


start = time.time()
result = set()
for t in range(-10000, 10001):
    if t%100 ==0:
        print "t=", t
    if two_sum(array, t):
        result.add(t)

end = time.time()
print "time:", (end-start)/60, "min"
print len(result)
print result

# for 10^10 array, the final searching time is about 4 hours
# number of t is 427
