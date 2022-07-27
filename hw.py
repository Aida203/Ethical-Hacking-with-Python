from cmath import pi
from turtle import width

from sklearn.metrics import balanced_accuracy_score

#1.1->1.3
class Circle:
    def __init__(self , raduis):  #constructor and there can only be 1 => no overloading
        self.raduis = raduis

    def getRaduis(self):
        return self.raduis
    
    def setRaduis(self , raduis):
        self.raduis = raduis
    
    def circleArea(self):
        return pow(self.raduis , 2) * pi

    def circleCircumference(self):
        return 2 * pi * self.raduis

    def displayCircleInfo(self):
        print(f"Raduis = {self.raduis} \n Area = {self.circleArea()} \n Circumfernce = {self.circleCircumference()}")


#1.3
class Rectangle:
    length=1.0
    width=1.0
    def __init__(self,length,width): #constr
        self.length=length
        self.width=width
    
    def __getLength__(self):
        return self.length
    def __setLength__(self,length):
        self.length=length
    def __setWidth__(self,width):
        self.width=width
    def __getArea__(self):
        return self.length*self.width
    def __getPerimeter__(self):
        return 2*(self.length+self.width)
    def __toString__(self):
        return (f" length= {self.length} \n width={self.width} \n area of rectangle={self.__getArea__()} \n perimeter={self.__getPerimeter__()}")


#rec=Rectangle(5,6)
#print(rec.__toString__())


#1.4
class Employee:
    id=999
    firstName="not given"
    lastName="None entered"
    salary=1

    def __init__(self,id,firstName,lastName,salary):
        self.id=id
        self.firstName=firstName
        self.lastName=lastName
        self.salary=salary

    def __getID__(self):
        return self.id
    def __getFirstName(self):
        return self.firstName
    def __getLastName(self):
        return self.lastName
    def __getName__(self):
        return self.firstName+"  "+self.lastName
    def __getSalary__(self):
        return self.salary
    def __setSalary__(self,salary):
        self.salary=salary
    def __getAnnualSalary(self):
        return 12*self.salary
    def __raiseSalary(self,percent):
        return (self.__getSalary__()+ (self.__getSalary__()*(percent/100)))
    
    def __toString__(self):
        return f"name : {self.__getName__()} \n id : {self.__getID__()} \n salary :  {self.__getSalary__()} \n annual salary : {self.__getAnnualSalary()}"


#em=Employee(13,"Ai","Aida",999)
#print(em.__toString__())

#1.6
class Account:
    id="656"
    name="not available"
    balance=0
    def __init__(self,id,name,balance):
        self.id=id
        self.name=name
        self.balance=balance
    
    def __getID__(self):
        return self.id
    def __getName__(self):
        return self.name
    def __getBalance__(self):
        return self.balance
    def __credit__(self,amount):
        self.balance+=amount
        return self.balance
    
    def __debit__(self,amount):
        if amount<=self.balance:
            self.balance-=amount
        else:
            print("Amount exceeded balance \n")
        return self.balance
    
    def _toString__(self):
        return f"Account [ id={self.id}, name = {self.name}, balance={self.balance}"


ac=Account("123","Aida",999)
print(ac._toString__())
