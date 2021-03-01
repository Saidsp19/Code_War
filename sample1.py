def allSubArrays(L,L2=None):
    if L2==None:
        L2 = L[:-1]
    if L==[]:
        if L2==[]:
            return []
        return allSubArrays(L2,L2[:-1])
    return [L]+allSubArrays(L[1:],L2)

def solve(arr):
    c = 0
    for i in arr:
        if (len(i)%2==0):
            arr1 = set(i)
            m = len(arr1)
            p = 0
            for j in arr1:
                k = i.count(j)
                if(k%2 == 0):
                    p = p+1
            if m==p:
                c = c+1
    print(c)

t = int(input())

for i in range(t):
    n = int(input())
    v = input()
    v = list(v)
    arr = allSubArrays(v)
    solve(arr)
