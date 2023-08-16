# Program to perform sorting slicing and string functions using python

n  = int(input("Enter the number of elements: "))
a = []
for i in range(n) :
    x = int(input())
    a.append(x)
    
a.sort()
print("sorted list : ", a)
print("sliced list", a[1:])
a = input("Enter the first string: ")
b = input("Enter another string: ")

#slicing
c = a + b
print("concatiated string is ", c)
print("string in upper case: ", a.upper())
print("String in capitalize: ", a.capitalize())
print("String in lowercase: ", c.lower());
j = input("enter the character to be replace for the string a")
print(a.find(j))
k = input("enter the new character which replace")
print(a.replace(j, k))


    