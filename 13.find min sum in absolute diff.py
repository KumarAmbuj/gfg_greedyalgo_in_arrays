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

def findminsum(arr1,arr2):
    n=len(arr1)
    Quicksort(arr1,0,n-1)
    Quicksort(arr2,0,n-1)

    sum=0

    for i in range(n):
        sum+=abs(arr1[i]-arr2[i])

    return sum

a = [3, 2, 1]
b = [2, 1, 3]
print(findminsum(a,b))

a = [4, 1, 8, 7]
b = [2, 3, 6, 5]
print(findminsum(a,b))