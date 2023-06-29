def fun(arr):
    countzero=0
    maxneg=-99
    minpos=99
    countneg=0

    prod=1

    n=len(arr)

    for i in range(len(arr)):

        if arr[i]==0:
            countzero+=1
            continue

        if arr[i]<0:
            countneg+=1
            maxneg=max(maxneg,arr[i])

        if arr[i]>0:
            minpos=min(minpos,arr[i])


        prod=prod*arr[i]


    if countzero==n  or(countneg==0 and countzero>0):
        return 0

    if countneg==0:
        return minpos

    if countneg&1==0 and countneg!=0:
        prod=(prod/maxneg)

    return prod


a = [ -1, -1, -2, 4, 3 ]
print(fun(a))

