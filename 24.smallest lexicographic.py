def findsmallest(arr,k):

    n=len(arr)

    for i in range(n-1):

        if k==0:
            return
        pos=i

        for j in range(i+1,i+k+1):

            if arr[j]<arr[pos]:
                pos=j

        k=k-pos+i

        for j in range(pos,i,-1):
            arr[j],arr[j-1]=arr[j-1],arr[j]


n, k = 5, 3

arr = [7, 6, 9, 2, 1]
findsmallest(arr, k)

for i in range(n):
    print(arr[i],end='')

print()

arr = [7, 6, 2, 9, 1]
findsmallest(arr, k)

for i in range(n):
    print(arr[i],end='')
print()
arr = [7, 2, 6, 9, 1]
findsmallest(arr, k)

for i in range(n):
    print(arr[i],end='')




