n=int(input("enter the limit:"))
list1=[]
for x in range(n):
    a=int(input("Enter the numbers:"))
    list1.append(a)
print("entered list of numbers:",list1)
list2=[x for x in list1 if x>0]
print("positive numbers:",list2)