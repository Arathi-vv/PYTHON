col1=['black','red','green']
col2=['red','blue','yellow']
print("The color list1:",col1)
print("The color llist2:",col2)
for i in range (len(col1)):
    if col1[i] not in col2:
        print("The color is:",col1[i])