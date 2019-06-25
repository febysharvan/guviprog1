a,b=map(int,input().split())
for z in range(a+1,b):
   if (z>1):
       for i in range(2,z):
           if (z%i) == 0:
               break
       else:
            print(z,end=" ")
