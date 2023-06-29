def Minheap():
    heap=[]
    return heap
def Add(heap,arr):
    for i in range(len(arr)):
        heap.append(arr[i])

    Buildminheap(heap)

def Heapify(heap,i,n):
    min=i
    l=2*i+1
    r=2*i+2

    if l<n and heap[l]<heap[i]:
        min=l

    if r<n and heap[r]<heap[min]:
        min=r

    if min!=i:
        heap[min],heap[i]=heap[i],heap[min]
        Heapify(heap,min,n)

def Buildminheap(heap):

    n=len(heap)

    for i in range((n-1)//2,-1,-1):
        Heapify(heap,i,n)

def Extractmin(heap):
    n=len(heap)
    min=heap[0]

    heap[0]=heap[n-1]
    heap.pop()
    n=len(heap)
    Heapify(heap,0,n)

    return min

def Insert(heap,x):
    heap.append(x)

    i=len(heap)-1

    while(i>0 and heap[i]<heap[i//2]):
        heap[i],heap[i//2]=heap[i//2],heap[i]
        i=i//2

def Size(heap):
    return len(heap)


def findmaxsum(arr,k):

    heap=Minheap()
    Add(heap,arr)

    for i in range(k):
        x=Extractmin(heap)

        x=(-1)*x
        Insert(heap,x)

    sum=0

    while(Size(heap)):
        x=Extractmin(heap)

        sum+=x
    return sum





arr = [3, -1, 9, 12, 2,-6]
k = 3
n = len(arr)
print(findmaxsum(arr,k))






