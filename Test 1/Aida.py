'''
Question 1-
1) List and tuples are both array like ways of storing data. Unlike
arrays the items contained can be of different data types.

The main difference is that unlike lists, tuples are not changeable
and items can not be individually deleted.

2)These are keywords which have different functions in loops.
The break statement is used to exit a loop, continue means to skip all statements after
the keyword and go to the enxt iteration after testing the condition,
the pass keyword is used in places in which we absolutely have to fill in statements
like in loops and functions.

3)Used to refer to the current object we are working with.


4) Meta-data for the string class

5)Inheritance is a concept in which a class can inherit / use the methods of 
another class. Consider the two classes below.


class A:
    def printHi(self):
        print("Hello from class A. I am the parent")

class B(A):
    def printWelcome(self):
        print("Welcome to class B.")

objectB=B()
objectB.printWelcome()
objectB.printHi()


Question 2-
1)T
2)T
3)T
4)T
5)F


Question 3-

1) 
def count_vowels(args):
    count =0
    for i in range(len(args)):
        if args[i]=='a' or args[i]=='e' or args[i]=='i' or args[i]=='o' or args[i]=='u' or args[i]=='A' or args[i]=='E' or args[i]=='I' or args[i]=='O' or args[i]=='U':
            count+=1
    return count


print(count_vowels("Celebration"))


2)



def sum_numbers(n):
    sum=0
    if n==1:
        sum=1
        return sum
    elif n==0:
        sum=0
        return sum
    else:
        sum+=sum_numbers(n-1)
        return sum

print(sum_numbers(2))    
   
   
3)

4)

   
sample_dict={'a':100,'b':200,'c':300}
for i in sample_dict.values():
    if i==200:
         print("Found")
         break
    else:
         print("Not found")




from math import pi

class Circle:
    __radius=1.0
    __color="red"
    def __init__(self,radius,color):
        self.radius=radius
        self.color=color
    
    def __getRadius__(self):
        return self.radius
    def __setRadius__(self,radius):
        self.radius=radius
    def __getColor__(self):
        return self.color
    def __setcolor__(self,color):
        self.color=color
    def __getArea__(self):
        return pi*self.radius*self.radius
    def __toString__(self):
        return f"Circle[ radius={self.radius},color={self.color},area={self.__getArea__()}]"

#m=Circle(2,"blue")
#print(m.__toString__())
    
class Cylinder(Circle):
    __height=1.0
    def __init__(self,radius,height,color):
        super().__init__(radius,color)

    def __getHeight__(self):
        return self.__height
    def __setHeight__(self,height):
        self.__height=height
    def __getVolume__(self):
        return pi*super().__getRadius__()*super().__getRadius__()*self.__getHeight__()


#n=Cylinder(5,2,"purple")
#print(n.__getVolume__())




#Question 4-


1)








#Question 5-

from multiprocessing.dummy import Array


1)
def __init__(self):  #default
    pass
def __init__(self,color):  #para
    self.color=color

2)

#class
class A:
    pass

#object of class A
m=A()
'''

import random 
import string


Uletters=(string.ascii_uppercase)
digits=(string.digits)
Lletters=(string.ascii_lowercase)
password=[]

random.shuffle(Uletters)
random.shuffle(digits)
random.shuffle(Lletters)

for i in range (round(len(Uletters)*0.4)):
    password.append(i)
for i in range (round(len(Lletters)*0.3)):
    password.append(i)
for i in range (round(len(digits)*0.3)):
    password.append(i)

print(f"Password is :{password[2:6]}")
