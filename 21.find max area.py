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


def findmaxarea(arr):
    n=len(arr)
    Quicksort(arr,0,n-1)

    for i in range(n//2):
        arr[i],arr[n-1-i]=arr[n-1-i],arr[i]

    sum=0
    l=0
    b=0
    flag=False

    i=0

    while(i<n-1):


        if i!=0:
            i+=1

        if (arr[i]==arr[i+1] or arr[i+1]-arr[i]==1) and flag==False:
            l=arr[i+1]
            flag=True
            i+=1

        if (arr[i]==arr[i+1] or arr[i+1]-arr[i]==1) and flag==True:
            sum+=(l*arr[i+1])
            i+=1
            flag=False

    return sum


a = [10, 10, 10, 10, 11, 10,
     11, 10, 9, 9, 8, 8]
n = len(a)

print(findmaxarea(a))



