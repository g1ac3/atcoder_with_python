N = input()
a = max(list(map(int,input().split())))
b = min(list(map(int,input().split())))
if a>b : print(0)
else : print(b-a+1)
