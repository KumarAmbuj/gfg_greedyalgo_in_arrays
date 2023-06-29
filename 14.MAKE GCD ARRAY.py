def makegcd(arr,k):

    result=0

    for i in range(len(arr)):
        if arr[i]!=1:
            result+=min(arr[i]%k,k-arr[i]%k)

        if arr[i]==1:
            result+=k-arr[i]

    return result

arr = [ 4, 5, 6 ]
n = len(arr)
k = 5
print(makegcd(arr, k))

arr = [ 4, 9, 6 ]
n = len(arr)
k = 5
print(makegcd(arr, k))