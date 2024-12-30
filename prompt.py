n=int(input("Enter the limit:"))
list1=[]
for x in range(n):
   x=int(input("Enter the numbers:"))
   if(x<100):
      list1.append(x)
   else:
      list1.append('over')
print(list1)