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
    while j < n2:
        marray[k] = arr2[j]
        j+=1
        k+=1
    #print marray, inversion
    return marray, inversion


def mergeSort_inversion(arr, inversion = 0):
    n = len(arr)
    if n <=1:
        return arr, inversion
    else:
        left, inversion = mergeSort_inversion(arr[0:n/2], inversion)
        right, inversion = mergeSort_inversion(arr[n/2:n], inversion)
        #print merge_inversion(left, right, inversion)
        return merge_inversion(left, right, inversion)

'''
#test case
output = mergeSort_inversion(c,0)
print output[1]
'''

array = []
with open("IntegerArray.txt", "r") as f:
    for line in f:
        array.append(int(line.strip()))

output =mergeSort_inversion(array)
print output[1]
print "length of array:", len(array)
