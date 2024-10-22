n = int(input("Enter the number of elements: "))  
my_list = []  
  
for i in range(n):  
    element = int(input("Enter element {}: ".format(i+1)))
    my_list.insert(i,element)  

print("List:", my_list)  

m = int(input("Enter the element which is to be appended in the list: "))
my_list.append(m)
print("List:", my_list) 

o = int(input("Enter the element which is to be removed in the list: "))
p = my_list.index(o)
del my_list[p]
print("List:", my_list)
