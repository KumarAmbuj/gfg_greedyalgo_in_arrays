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


def findminsum(arr):
    sum=0
    n=len(arr)
    Quicksort(arr,0,n-1)
    i=0
    a=0
    b=0

    while(i<n):
        a=a*10+arr[i]
        i+=1
        if i<n:
            b = b * 10 + arr[i]
            i += 1


    return a+b

a=[6, 8, 4, 5, 2, 3]
print(findminsum(a))

b=[5, 3, 0, 7, 4]
print(findminsum(b))

