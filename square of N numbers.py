n=int(input(print("enter the limit of numbers:")))
list1=[]
for i in range(n):
   a=int(input(print("enter the number:")))
   list1.append(a)
list2=[x**2 for x in list1]
print(list2)