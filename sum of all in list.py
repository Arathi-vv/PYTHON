list=[]
sum=0
limit=int(input("Enter the limit:"))
print("Enter ",limit,"numbers:")
for i in range(limit):
    list2=int(input())
    list.append(list2)
for i in list:
    sum=sum+i
print("sum of list:",sum)