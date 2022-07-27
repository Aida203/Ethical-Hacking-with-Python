import os

cmd=input("Enter command and ## to leave \n")

while True:
    if  cmd=="##":
        print("BYE BYE")
        os.abort()
        
    os.system(cmd)
    cmd=input("Enter command and exit to leave \n")
