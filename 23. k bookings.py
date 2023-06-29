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

def isPossible(arv,depar,k):
    n=len(arv)
    Quicksort(arv,0,n-1)
    Quicksort(depar,0,n-1)

    m=1
    j=depar[0]

    for i in range(1,len(arv)):

        if arv[i]<j:
            m+=1

        j=depar[i]

    return m==k


arrival = [1, 3, 6]
departure = [2, 6, 8]
n = len(arrival)

if isPossible(arrival,departure, 1):
    print("Yes")
else:
    print("No")
