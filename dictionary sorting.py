my_dict={'apple':5,'banana':2,'orange':8,'grape':3}
asc=dict(sorted(my_dict.items()))
print("Ascending order:",asc)
dsc=dict(sorted(my_dict.items(),reverse=True))
print("Descending order:",dsc)