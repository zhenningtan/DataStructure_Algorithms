# merge sort function
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

# test case
c = [4,5,10, 9,6,8, 1,2,3]


print mergeSort(c)

############################################################
# Count inversion
# merge sort function
def merge_inversion(arr1, arr2, inversion):
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
            inversion += (n1-i)
        k +=1
    # add the remaining elements of arr1 or arr2 to the sorted array if any
    while i < n1:
        marray[k] = arr1[i]
        i+=1
        k+=1
        inversion += (n1-i)
    while j < n2:
        marray[k] = arr2[j]
        j+=1
        k+=1
    return marray, inversion

print "Test case:"
a= [4,5,6]
b= [1,2,3]
print merge_inversion(a,b)
print ""

def mergeSort_inversion(arr, inversion = 0):
    inversion = inversion 
    n = len(arr)
    if n <=1:
        return arr
    else:
        left, inversion = mergeSort(arr[0:n/2], inversion)
        right, inversion = mergeSort(arr[n/2:n], inversion)
        return merge_inversion(left, right, inversion)




c = [4,5,6, 1,2,3]
output = mergeSort_inversion(c,0)
print output
