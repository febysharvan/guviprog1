x,y=map(int,input().split())
rem=0
sum=0
a=0
for anos in range(x+1,y):
    a=anos
    while(anos>0):
     rem=anos%10
     sum+=rem**3
     anos=anos//10
    if(a==sum):
        print(a,end=" ")
    sum=0
