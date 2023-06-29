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
        q = partition(arr, p, r)
        Quicksort(arr,p,q-1)
        Quicksort(arr,q+1,r)

def pyramid(arr):
    n = len(arr)

    Quicksort(arr,0,n-1)

    h=0
    sum=0
    i=1


    while(sum<n):
        sum+=i
        if sum>n:
            break
        else:
            i+=1
            h+=1

    return h

arr = [10, 20, 30, 50, 60, 70,89]
print(pyramid(arr))

arr = [40, 100, 20, 30]
print(pyramid(arr))
