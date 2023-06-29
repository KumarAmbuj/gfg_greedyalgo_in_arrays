#using heap
def Minheap():
    heap=[]
    return heap

def Add(heap,arr):
    for i in range(len(arr)):
        heap.append(arr[i])

    Buildminheap(heap)

def Buildminheap(heap):
    n=len(heap)

    for i in range((n-1)//2,-1,-1):
        Heapify(heap,i,n)

def Heapify(heap,i,n):
    min=i

    l=2*i+1
    r=2*i+2

    if l<n and heap[l]<heap[i]:
        min=l

    if r<n and heap[r]<heap[min]:
        min=r

    if min!=i:
        heap[i],heap[min]=heap[min],heap[i]
        Heapify(heap,min,n)

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


def findsuminpair(arr):
    sum=0

    heap=Minheap()
    Add(heap,arr)

    while(Size(heap)>1):

        x=Extractmin(heap)
        y=Extractmin(heap)

        if x<y:
            sum+=x
            Insert(heap,x)
        elif x>y:
            sum+=x
            Insert(heap,y)

    return sum


A = [7, 2, 3, 4, 5, 6]
print (findsuminpair(A))
