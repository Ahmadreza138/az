n=int(input())
x=True
for i in range(2,n):
    if n%i==0:
        x=False
        break
if x:
    print('Yes')
else:
    print('No')
