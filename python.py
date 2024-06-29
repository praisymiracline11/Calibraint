print("PYTHON VARIABLES")

# python variables

# assigning two variables seperately and printing them
stu_name="praisy"
age=20
print(stu_name,"is",age)

# assigning multiple values in single line and printing them
name,age,city="praisy",20,"chennai"
print(name)
print(age)
print(city)

print("DATA TYPES")

# data types in python

# printing the data types with examples for each data type
x=20
print(type(x))

y=20.8
print(type(y))

z="praisy"
print(type(z))

mylist=[20,20.8,"praisy"]
l=type(mylist)
print(l)

tuple=(20,20.8,"praisy",11)
t=type(tuple)
print(t)

myset1={"blue","green","orange","white"}
ms1=type(myset1)
print(ms1)

myset2=frozenset({"blue","green","orange"})
ms2=type(myset2)
print(ms2)

dict={"name":"praisy","age":20,"city":"chennai"}
d=type(dict)
print(d)

print("TYPECASTING")

# typecasting in python

# specifying the data types of variables and printing them
# variables are defined above
print(str(name))
print(int(age))
print(float(y))
print(float(x))
print(int(y))

print("CONDITIONALS")

# checks the two numbers with condition

num1=20
num2=11

# according to the given if condition it checks the condition 
# and then prints the given print statement
# checks whether num1 is greater
if num1>num2:
 print("num1 is greater")

# checks whether num2 is smaller
if num2<num1:
 print("num2 is smaller")

# checks whether num1 and num2 are equal 
if num1==num2:
 print("num1 and num2 are equal")
else :
 print("num1 and num2 are not equal")

#  checks whether num1 and num2 are not equal
if num1!=num2:
 print("num1 and num2 are not equal")
elif num1==num2:
 print("num1 and num2 are equal")

print("FUNCTIONS")

#functons in python


def errortype(type):
 print(type + " error")
errortype("syntax")
errortype("type")
errortype("name")
errortype("index")
errortype("key")
errortype("value")

print("BUILTIN FUNCTIONS")

print("min of num1,num2 is ",min(num1,num2))
print("min of x,y is ",min(x,y))
print("max of num1,num2 is ",max(num1,num2))
print("max of x,y is ",max(x,y))
print("absolute value of y is ",abs(y))
print("length ",len(city))
print("length ",len(z))
list=["blue","green","orange"]
print("list= ",list)
list.append("brown")
list.append("grey")
list.append("pink")
list.insert(0,"white")
print("list= ",list)
list.remove("pink")
print("list= ",list)

print("LISTS")

list1=["praisy","raje","pooja",11]
list2=["sanjay","mals","sas",19]
print("list1= ",list1)
print("list2= ",list2)
list1.append("priya")
print("list1= ",list1)
list2.insert(3,"praisy")
print("list2= ",list2)
a=len(list1)
b=len(list2)
print(a)
print(b)
list2.remove("praisy")
list1.extend(list2)
print("list1= ",list1)
print("list2= ",list2)
c=type(list1)
print(c)

print("TUPLES")

tuple1=("blue","green","orange","brown","white","grey",11,19)
print("tuple1= ",tuple1)

print("SETS")

set={"apple","cherry","strawberry"}

