
n=int(input("Enter the limit:"))
mylist=[]
for i in range(n):
    a=int(input("enter the list elements:"))
    mylist.append(a)
mylist=[x for x in mylist if x%2!=0]
print(mylist)