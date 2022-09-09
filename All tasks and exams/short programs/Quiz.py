'''
#Q3
#1 Palindrome
txt=input("Enter the word \n")
rev=txt[::-1]
print("Palindrome") if txt==rev else print("not palindrome")


#2 List with even and odd
l1=[10,20,25,30,35]
l2=[40,45,60,75,90]
odd=[]
even=[]
for i in l1:
    if i%2!=0: odd.append(i) 

for i in l2:
    if i%2==0: even.append(i) 

list=even+odd
list.sort()
print(list)


#3 exponent(base,exp)
def exponent(base,exp):
    if exp==0: return 1
    return base**exp

print(exponent(2,2))


#4 multiplication table
def multiplicationTable(num):
    print(f"Multiplication table to 10 of the number {num}") 
    i=1
    for i in range(11) :
        print(f"{i} * {num}  =  {i*num}")

multiplicationTable(2)


#5 reverse using loop
l1=[10,20,25,30,35]
i=len(l1)-1
while i>=0:
    print(l1[i])
    i-=1


#6 prime numbers in a range
def primeNumbers(start,stop):
    if start==1 or stop==1:
        return("Please enter a number >1")
    count=0
    list=[]
    for i in range (start+1,stop,1):
        n=i
        while n>start and n<stop:
            if i%n==0:
                count+=1
            n+=1
        if count<=1:
            list.append(i)
    
    print(list)

primeNumbers(2,5)


#7 Fizz buzz



#8  same tuple content
t1=(1,1,1,1)
count=0
f=t1[0]
limit=len(t1)
for i in range (0,len(t1)):
    if i==limit:
        break
    if f==t1[i]:
        count+=1

print(count==len(t1))


#combination

#nCr= n!/( r!(n-r)!)

def factorial(n):
    if n==1: return 1
    i=n
    sum=1
    while i>0:
        sum*=i
        i-=1
    return sum

def combination(n,r):
    N=factorial(n)   #n!
    R=factorial(r)   #r!
    NR=factorial(n-r)  #(n-r)!
    return N//(R*NR)

print( combination(5,2))

'''
#Was not able to come up with the Fibonacci










