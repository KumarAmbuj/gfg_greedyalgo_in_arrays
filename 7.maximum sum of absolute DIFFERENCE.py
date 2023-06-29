def partition(arr,p,r):
    x=arr[r]
    i=p-1

    for j in range(p,r):
        if arr[j]<x:
            i+=1
            arr[j],arr[i]=arr[i],arr[j]
    arr[i+1],arr[r]=arr[r],arr[i+1]
    return i+1


def Quicksort(arr,p,r):
    if p<r:
        q=partition(arr,p,r)
        Quicksort(arr,p,q-1)
        Quicksort(arr,q+1,r)

def findmaxsum(arr):
    Quicksort(arr,0,len(arr)-1)



    n=len(arr)

    arr1=[]
    i=0
    while(i<=(n//2)):
        arr1.append(arr[i])
        arr1.append(arr[n-1-i])
        i+=1

    sum=0
    for i in range(len(arr1)-1):
        sum+=abs(arr1[i]-arr1[i+1])

    sum+=abs(arr1[n-1]-arr1[0])

    return sum


a = [ 1, 2, 4, 8]
print(findmaxsum(a))