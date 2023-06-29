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

def maximize(arr):
    n=len(arr)
    Quicksort(arr,0,n-1)

    sum=0

    for i in range(len(arr)):
        sum=sum+arr[i]*i

    return sum

arr = [3,5,6,1]
n = len(arr)
print(maximize(arr))