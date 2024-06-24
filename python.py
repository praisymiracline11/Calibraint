print("PYTHON VARIABLES")

stu_name="praisy"
age=20
print(stu_name,"is",age)

name,age,city="praisy",20,"chennai"
print(name)
print(age)
print(city)

print("DATA TYPES")

x=20
print(type(x))
y=20.8
print(type(y))
z="praisy"
print(type(z))
mylist=[20,20.8,"praisy"]
tuple=(20,20.8,"praisy",11)
set1={"blue","green","orange","white"}
set2=frozenset({"blue","green","orange"})
dict={"name":"praisy","age":20,"city":"chennai"}

print("TYPECASTING")

print(str(name))
print(int(age))
print(float(y))
print(float(x))
print(int(y))

print("CONDITIONALS")

num1=20
num2=11
if num1>num2:
 print("num1 is greater")
if num2<num1:
 print("num2 is smaller")
if num1==num2:
 print("num1 and num2 are equal")
else :
 print("num1 and num2 are not equal")
if num1!=num2:
 print("num1 and num2 are not equal")
elif num1==num2:
 print("num1 and num2 are equal")

print("FUNCTIONS")

def errortype(type):
 print(type + " error")
errortype("syntax")
errortype("type")
errortype("name")
errortype("index")
errortype("key")
errortype("value")

print("BUILTIN FUNCTIONS")

print(min(num1,num2))
print(min(x,y))
print(max(num1,num2))
print(max(x,y))
print(abs(y))
print(len(city))
print(len(z))
list=["blue","green","orange"]
print(list)
list.append("brown")
list.append("grey")
list.append("pink")
list.insert(0,"white")
print(list)
list.remove("pink")
print(list)

print("LISTS")

list1=["praisy","raje","pooja"]
list2=["sanjay","mals","sas"]
print(list1)
print(list2)
list1.append("priya")
print(list1)
list2.insert(3,"praisy")
print(list2)
a=len(list1)
b=len(list2)
print(a)
print(b)
list2.remove("praisy")
list1.extend(list2)
print(list1)
print(list2)
c=type(list1)
print(c)