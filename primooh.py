a=int(input())
yesh=0;
for j in range(2,a):
    if(a%j==0):
        yesh=1 
if(yesh==1):
    print("no")
else:
    print("yes")
