z=int(input(""));
i=0;
while(1):
    b=z%10;
    z=z/10;
    if(z>1):
       i=i+1;
    else:
        print(i+1);
        break
