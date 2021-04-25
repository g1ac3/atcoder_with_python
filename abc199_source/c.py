n = int(input())
s = list(input())
q = int(input())
rev = int(1)
for i in range(q):
    t,a,b = map(int,input().split())
    if t == 2:
        rev *= -1
        continue;
    a -=1
    b -=1
    if rev < 0 :
        a = (a+n)%(2*n)
        b = (b+n)%(2*n)
    s[a],s[b] = s[b],s[a]
if rev < 0:
    s = s[n:]+s[:n]
for x in s:
    print(x,end='')
