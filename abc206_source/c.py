N = int(input())
A = list(map(int,input().split()))
A.sort()
st = int(1)
sum = int(0)
for i in range(N-1):
    if A[i] == A[i+1]:
        st+=1
    else:
        sum = sum + ((N-i-1)*st)
        st = 1
print(sum)
# list.sort()
