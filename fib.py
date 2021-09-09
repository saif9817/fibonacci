#the following is a significantly faster alternative to recursive fibonacci, this is done by storing the previous two numbers allowing for the removal of all recursion and duplicate calls
#this is expected to be linear runtime

def fib(x):
    if x<=1:
        return x
    else:
        arr = [0,1] #this array stores our fib numbers, only 2 are required to be stored
        y=1         #counter variable
        while(y<x): 
            temp = arr[1]
            arr[1] = arr[0]+arr[1]
            arr[0] = temp
            y+=1
        return arr[1]
print("This program will give you the nth fibonacci number, n being your input")
print("=======================================================================")
flag = True
while(flag):
    req = input("Please enter a number: ")
    print(fib(int(req)))
    text = input("Do you want to quit? y/n ")
    if text == "y":
        flag = False
    
