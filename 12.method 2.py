def findminsuminpair(arr):
    n=len(arr)

    mn=99
    for i in range(n):
        mn=min(mn,arr[i])

    return mn*(n-1)

A = [7, 2, 3, 4, 5, 6]
print (findminsuminpair(A))