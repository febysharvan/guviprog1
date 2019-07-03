l=int(input())
s=list(map(int,input().split()[:l]))
s.sort()
for i in s:
    print(i,end=" ")
