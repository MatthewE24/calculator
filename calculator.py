# global variables

param1=0
param2=0
op ="+"
x=1

# function definition
def intro():
    print("Welcome to THE calculator")
    return

def inputBoi():
    global param1
    global param2
    global op
    param1 = input("what is your first parameter?")
    param2 = input("what is your second parameter?")
    op = input("what is your operator?")
    return

def calculate():
    global op
    if(op=="+"):
       print(int(param1)+int(param2))
    elif(op=="-"):
       print(int(param1)-int(param2))
    elif(op=="*"):
       print(int(param1)*int(param2))
    elif(op=="/"):
       print(int(param1)/int(param2))
    return

def end():
    global x
    y=input("would you like to continue")
    if(y=="yes"):
        x=1
    else:
        return
    
    
#execution code
intro()
while(x==1):
    inputBoi()
    calculate()
    end()
