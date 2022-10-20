from cgi import print_form


n=int(input("Enter the number of elements in the list:"));
list=[];
for i in range(0,n):
    elements=int(input("Enter the elements in the list:"));
    list.append(elements);
a=int(input("Enter the number to search in the list:"));
if a in list:
    print("Element found in the List");
else:
    print("Element not found in the list");