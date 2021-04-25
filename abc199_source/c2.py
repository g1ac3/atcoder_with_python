n = int(input())
s = list(input())
q = int(input())
rev = int(1)
for i in range(q):
    t,a,b = map(int,input().split())
    if t == 2:
        s = (s[n:]+s[:n])
    else :
        a = a-1
        b = b-1
        s[a],s[b] = s[b],s[a]
for x in s:
    print(x,end='')
