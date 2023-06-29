def partition(arr,p,r):
    x=arr[r]
    i=p-1

    for j in range(p,r):
        if arr[j]<x:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[r]=arr[r],arr[i+1]
    return i+1


def Quicksort(arr,p,r):
    if p<r:
        q=partition(arr,p,r)
        Quicksort(arr,p,q-1)
        Quicksort(arr,q+1,r)

def findmaxdiff(arr,k):
    n=len(arr)
    Quicksort(arr,0,n-1)

    arr1=arr[:k]
    arr2=arr[k:]

    diff=abs(sum(arr2)-sum(arr1))

    return diff
arr = [8, 4, 5, 2, 10]
k = 2
print(findmaxdiff(arr,k))
