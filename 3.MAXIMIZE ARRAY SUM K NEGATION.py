def findmaxsum(arr,k):

    for i in range(k):
        index=-1
        min=999

        for j in range(len(arr)):

            if arr[j]<min:
                min=arr[j]
                index=j

        if min==0:
            break

        arr[index]=-(arr[index])

    sum=0

    for i in range(len(arr)):
        sum+=arr[i]
    return sum

arr = [-6, -1, 9, 12, 2]
k = 3
n = len(arr)
print(findmaxsum(arr,k))

