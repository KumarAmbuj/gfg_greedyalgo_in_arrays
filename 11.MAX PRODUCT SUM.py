def findminsumprod(arr1,arr2,k):
    sum=0
    mx=-9
    index=-1


    for i in range(len(arr2)):

        if abs(arr2[i]>mx):
            mx=abs(arr2[i])
            index=i



    prod=arr1[index]*arr2[index]

    if prod<0 and arr1[index]<0:
        arr1[index]=arr1[index]-2*k
    elif prod<0 and arr2[index]<0:
        arr1[index]=arr1[index]+2*k
    elif prod>0 and arr1[index]<0:
        arr1[index]=arr1[index]+2*k
    elif prod>0 and arr1[index]>0:
        arr1[index]=arr1[index]-2*k

    sum=0
    for i in range(len(arr1)):
        sum+=arr1[i]*arr2[i]

    return sum







a = [ 2, 3, 4, 5, 4 ]
b = [ 3, 4, 2, 3, 2 ]
n = 5
k = 3
print(findminsumprod(a,b,k))
