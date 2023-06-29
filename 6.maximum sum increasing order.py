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


def findmaxsum(arr):

    n=len(arr)
    m=len(arr[0])

    for i in range(len(arr)):
        Quicksort(arr[i],0,len(arr[i])-1)

    sum=arr[n-1][m-1]
    prev=arr[n-1][m-1]


    for i in range(n-2,-1,-1):

        for j in range(m-1,-1,-1):

            if arr[i][j]< prev:
                sum+=arr[i][j]
                prev=arr[i][j]
                break
            elif j==0 and arr[i][j]>=prev:
                return 0
    return sum



arr = [[1, 7, 3, 4],
       [4, 2, 5, 1],
       [9, 5, 1, 8]]

print(findmaxsum(arr))


arr = [[9, 8, 7],
                   [6, 5, 4],
                   [3, 2, 1]]
print(findmaxsum(arr))





