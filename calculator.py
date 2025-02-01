usernum = input("1: add 2: subtract 3:multiply 4:devide")

def add(usernum1,usernum2):
    print(usernum1+usernum2)
def subtract(usernum1,usernum2):
    print(usernum1-usernum2)
def multiply(usernum1,usernum2):
    print(usernum1*usernum2)
def devide(usernum1,usernum2):
    print(usernum1/usernum2)

usernum1 = int(input("what is you first number?"))
usernum2 = int(input("what is your second number?"))
if usernum == "1":
    add(usernum1,usernum2)
elif usernum == "2":
    subtract(usernum1,usernum2)
elif usernum == "3":
    multiply(usernum1,usernum2)
elif usernum == "4":
    devide(usernum1,usernum2)
