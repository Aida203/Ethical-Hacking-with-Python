'''switch cases : A way to compare a data type and take some actions based on the nature(content) of this variable. 
                Python does not have switch cases but the alternative is DICTIONARY MAPPING, if-else statements, python classes
                , functions and lambdas.


'''
#Dictionary mapping : Mapping keys to values or values to keys

n1=int(input("Enter a number\n"))
n2=int(input("Enter another number\n"))

d={0:"Addition", 1:"Multiplication",2:"Division"}

print("Choose an operation number\n")
print(d)
n=int(input())
if n==0:
    print(f"{d[0]} =>",n1+n2)
elif n==1:
    print(f"{d[1]} =>",n1*n2)
elif n==2:
    print(f"{d[2]} =>",n1//n2)
else:
    print("Invalid operation")


#To print all keys of a dictionary
print(d.keys())

#To print all values
print(d.values())

#To print both
print(d.items())

'''
#Classes and Objects in python
#An object is a collection od data and methods which can act on these data. A class is a blueprint of an object.


class myFirstClass:

    def __init__(self,name):  #does actions to objects which are just initialized  and self is just a reference to the current class
        self.name=name
    
    def printAWord(self):
        print(f"Apple from  {self.name}'s garden")

m=myFirstClass("Aida")

print(m.name)
m.printAWord()

#delete an object'\s property
del m.name

#delete an object
del m



#Lambdas
#Can take any digit but only one expression which will be executed and result returned
#multiplication of a number by 2
m=lambda a:a*2
print(m(5))

y=lambda a,b: a*b
print(y(2,3))

#can be used as a return of a function
def multi(n):
    return lambda a:a*n

x=multi(2)
print(x(3))

'''
