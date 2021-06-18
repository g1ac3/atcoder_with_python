N = int(input())
a = list(map(int,input().split()))
a.sort()
t = True
for i in range(0,N):
    if a[i] != i+1:
        t = False
if t==True:
    print('Yes')
else:
    print('No')
# boolの頭文字大文字
#配列入力list(map(型,input().split()))
#splitないと' ' が配列の間に入る
