'''my_list=["aapple","banana",1,3,5,7]
my_list[2:5]="abc"
print(my_list)
my_list=[1,2,4,5,6]
my_list.insert(2,3)
my_list.append("ksbckj")
list1=[1,2,3]
list2=[4,5,6]
list1.extend(list2)
#remove
list1=[1,2,3,"apple",4,5,6]
list1.remove("apple")
list1.pop(3)
print(list1)
my_list=[1,2,3,4,5,6]
my_list.insert(2,"apple")
print(my_list)
my_list.append(7)
print(my_list)
#loopslists
list=[1,2,3,4,4,4,5,6]
for X in list1:
   print(X)
#sort
list=[2,5,1,4,8]
list.sort()
print(list)
list=[2,5,1,4,8]
list.sort(reverse=True)
print(list)
#common string methods:
text='HELLO python'
print(text.upper()) #smaller cased gets capitalised
print(text.lower()) #capital letters gets lower cased
print(text.strip()) #removes spaces from start and end 
print(text.replace('python','WORLD')) #replaces substring with another
print(text.split()) #splits string into a list

#FOREST STRING 

# 1. using f-strings

Name="bob"
Age=20
print(f"My name is (Name) and age is (Age)")


x=5
X+=5
X-=5
X*=4
#aeithemetic operator
X/=7
x%=10
X**=5
X//=7
#comaprison operators
print(5==5)
print(5!=3)
print(5>3)
print(5<3)
print(5>=5)
print(5<=4)
 #logical operators
X=5
print(x>3 and X<10) #True
print(not(x>3))   #false
#identitiy operators
X=8
Y=X
Z=10
X is Y
X is not Y
# print(y)
print(X is Y)
print(X is not Y)


#sets
colors={"red","green","blue"} #creating a set
print(colors)

colors.add("yellow") #adding elements
print(colors)

colors.remove("green") #removing elements
print("colors")

for color in colors: #iterating through set
 print(color)

 #dictionaries
 student={"name":"alice","age":20,"grade":"A"}
 print(student)

 print(student["name"]) #alice  #
print(student.get("age")) #20

student["age"] =21  #accessing values
student["city"] ="delhi"
print(student)

student.pop("grade")  #removing items
del student["city"]
print(student)

for key,value in student.items():  #iterating through dictionary 
   print(key,":",value)


 #if else 
age=20

if age>=18:
     print("you are adult")

elif age==18:
   print("you are a teen")

elif age==17:
    print("you are 17")
else:     
     print("you are not adult")

x=15

if x>10:
   print("x is greater than 10")

   if x>20:
      print("x is greater than 20")
   else:
        print("x is greater than 20")

'''
# x=int(input())
# if x%2==0:
#       print("given number is even")
# else:
#     print("given number is odd")
# '''
#loops
# fruits=["apple","banana","cherry"]
# for i in fruits:
#       print(i)

# word="python"

# for i in word:
#     print(i)
# print()
# for i in range(1,11):
#     print(i)
# print()
# for i in range(1,10,2):
#     print(i)

# for i in range(1,4):
#      for j in range(1,3):
#          print(f"i={i},j={j}")

# for i in range(1,6):
#      if i==4:
#          break
#      print(i)
 
#  #questions 1
# for i in range(1,21):
#      print(i)

#  #questions 2
# for i in range (0,30,2):
#      print(i)

# #Functions

# def greet(name):
#     print(f"hello ,{name}")

# greet("alice")
# greet("bob")
# i=1,j=1
# i=1,j=2
# i=2,j=1
# i=2,j=2
# i=3,j=1
# i=3,j=2

# def add(a,b):
#     return a+b
# result=add(7,4)
# print(result)
# def sub(a,b):
#     return a-b
# def product(a,b):
#     return a*b
# def divide(a,b):
#     return a/b
# def greet(name="student"):
#     print(f"hello,{name}")
# greet()
# greet("alice")
# x=10 #global
# def my_func():
#     y=5
#     global X 
#     print("inside",x,y)
# my_func()

# #questions1
# def greet():
#     print("Hello")

# #questions2
# def add(a,b):
#     print(a+b)

# #questions7
# x=10
# def demo():
#     y=4
#     print(y,"local")
#     print(x,"global")
#     print(x+y)
 

# #class
# class Car:
#     def int__(self,brand,color):
#      self.brand=brand #attributes
#      self.color=color #attributes
# def drive(self): #method
#       print(f"{self.color}{self.brand}is driving 🚗")

# #objcarect
# car1 =Car("BMW","Black")
# car2 =Car("Tesla","White")


# car1.drive()
# car2.drive()


# #Array

# import array as sir

# #create array of integers

# numbers=sir.array('i',[1,2,3,4,5])
# print(numbers)

# #numpy

# from numpy import random

# x=random.randint(100)
# print(x)#x=random.randint(100)
# x=random.rand()
# print(x)
# print(type(x))

# [54]  #0-D array
# [1,2,3,4,5,]  # 1-D array

# [[1,2,3,]],  # 2-D array
# [4,5,6,]

# [[[1,2,3,]]],  # 3-D array
# [[4,5,6,]]
# [[7,8,9,]]
# [10,11,12]

from numpy import random
x=random.randint(100,size=(3,5))
print(x)

x=random.randint(100,size=(2,3,5))   #row,coloum
print(x)

x=random.randint(100,size=(2,2,3,5))  #row,coloum
print(x)

x=random.choice([4,5,6] , size=(5))
print(x)

x=random.choice([4,5,6] , size=(2,3,5))
print(x)



# '''
import pandas as pd
data=[10,20,30,40]
S=pd.Series(data)
print(S)

##################
data={
    "name":["Alice","Bob","Charlie","David"],
    "Age":[24,27,22,32],
    "City":["Delhi","Mumbai","Chennai","Kolkata"]
}
df=pd.DataFrame(data)
print(df)


import numpy as np
arr=np.array([1,2,3,4,5])
s=pd.series(arr)
print(s)


data={"Maths":90,"Science":85,"English":78}
s=pd.Series(data)
print(s)

import pandas as pd
df=pd.read_csv("crocodile_dataset.csv")
print(df.head())
print(df.tail)
























    

  









         
    
                    
    

    















 












      