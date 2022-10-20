n=int(input("Enter the number of elements in the list:"));
list=[];
for i in range(0,n):
    elements=int(input("Enter the elements in the list:"));
    list.append(elements);
    for j in range(0,n-i):
        list.sort();
print(list,end=" ");