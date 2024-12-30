n=int(input("Enter the limit:"))
l=[]
c=0
for x in range(n):
     x=input("enter a name:")
     l.append(x)
for i in l:
     for j in i:
         c=c+1
print("Occurance of 'a' is:",c)