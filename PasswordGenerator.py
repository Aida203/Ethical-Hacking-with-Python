import string  

import random



#define list of letters, digits and special characters

letters=list( string.ascii_letters ) #gets all letters, upper and lowercases

digits=list(string.digits) # 0----9

chars= list( string.punctuation) #special characters

print("Welcome , let's have function: ")

def generatePassword():
    #Ask user to enter the passwprd length
    passwordLength=input("Enter the password length \n")

    while True:

        try:
          #for code which may give errors
          # check passwordLength is int and >=8
            passwordLength=int(passwordLength)

            #if user enters a char or <8 we want to ask for a new input   =>that's why we are in the while loop
            if passwordLength<8:
                print("Sorry but your password must be at list 8 characters \n")

                passwordLength=int(input("Enter the password length \n"))


            if passwordLength>=8:
                break

           
        except:
            print("Please enter numbers only \n")  #in case the user enters a string for example

            passwordLength=int(input("Enter the password length \n"))
    #definning a list of password this will be a mix of digits, special chars, string . It should be random and that is why we import the random library
    #This library contains a function called shuffle 

    password=[]

    random.shuffle(letters)
    random.shuffle(digits)
    random.shuffle(chars)

    #after shuffling we want to append these in the list

    #remember we want a mix of all of these => we need a loop for each to get like 60%
    #letters, 30%digits and 10%chars


    #appending letters in to password and remember we want 60% of it
    #=> 60% of password length as we never kow how long it will be
    for i in range( round( passwordLength * .6 ) ):
        password.append(letters[i])

    #appending digits in to password and remember we want 30% of it

    for i in range( round( passwordLength * .3 ) ):
        password.append(digits[i])

#appending special chars in to password and remember we want 10% of it

    for i in range( round( passwordLength * .1 ) ):
        password.append(chars[i])
    
    #Joinning the password as one string not individual
    password="".join(password)[0:] #first index till the end => put whole list in the password
    print(f"Your password is  :   {password}")


generatePassword()








