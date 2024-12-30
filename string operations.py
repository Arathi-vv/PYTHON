list1=[1,2,3,4,5,6]
list2=[8,7,6,5]
print("The first list:",list1)
print("The 2nd list:",list2)
if len(list1)==len(list2):
    print("The 2 list have same length")
else:
    print("The 2 list have diffrent length")
s1=0
s2=0
for i in range(len(list1)):
    s1=s1+list1[i]
print("The sum of first list:",s1)
for i in range(len(list2)):
    s2=s2+list2[i]
print("The sum of 2nd list:",s2)
if s1==s2:
    print("The sum of list is same")
else:
    print("The sum of list is diffrent")
print("The common Elements")
for i in list1:
    for j in list2:
        if i==j:
            print(i)