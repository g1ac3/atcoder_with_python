N,Q = map(int,input().split())
A = list(map(int,input().split()))
B = [A[0]-1]
for i in range(1,N):
    B.append(B[i-1]+A[i]-A[i-1]-1)
#print(B)
for i in range(Q):
    k = int(input())
    if k > B[N-1]:
        print(k+N)
    elif k < A[0]:
        print(k)
    else:
        l=int(0)
        r=int(N)
        while (r-l)>1:
            c=int((r+l)/2)
            #print(l,r,c)
            if B[c] >= k:
                r = c
            else:
                l = c
        print(A[l+1]-1+k-B[l+1])
#intキャスト忘れない
