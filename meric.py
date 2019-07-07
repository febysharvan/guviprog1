x,y=input().split()
if(len(x)!=len(y)):
    print("no")
for i in range (len(x)):
    x=x.replace(x[i],y[i])
if(x==y):
    print("yes")
else:
    print("no")
