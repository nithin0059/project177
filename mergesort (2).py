def mergesort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    left=mergesort(left)
    right=mergesort(right)
    return merge(left,right)
def merge(left,right):
    new=[]
    i=0
    j=0
    while i<len(left)and j<len(right):
        if left[i]<right[j]:
            new.append(left[i])
            i+=1
        else:
            new.append(right[j])
            j+=1
    new.extend(left[i:])
    new.extend(right[j:])
    return new
array=[8,9,2,5,7,1,6,4,3,0]
print("unsorted array is: ",array)
sorted_array=mergesort(array)
print("sortred array is: ",sorted_array)
