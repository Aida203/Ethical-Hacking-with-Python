import os  #provides fxns to create and remove a directory(folder),fetching its 
            #contents,changing and identifying current directory,etc

cmd=input("Enter command and ## to leave \n")

while True:
    if  cmd=="##":
        print("BYE BYE")
        os.abort()  #stops program
        
    os.system(cmd) #executes the command in subshell, input parameter is a string 
                   #and output is the value returned by the system shell for windows (output varries per system)
    cmd=input("Enter command and exit to leave \n")
