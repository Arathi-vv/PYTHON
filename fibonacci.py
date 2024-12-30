f1=0
f2=1
limit=int(input("enter the limit:"))
print("The fibnacci series up to",limit,"terms are:")
print(f1)
print(f2)
for i in range(limit-2):
    f3=f1+f2
    f1=f2
    f2=f3
    print(f3)