a,b=map(int,input().split())
c=list(map(int,input().split()))
d=c[0:int(a)]
sum=0
for i in range(b):
    sum=sum+d[i]
print(sum)
