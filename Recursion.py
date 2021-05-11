#Recursion=calling the function from the same function

def DispalyIF(no):
    for i in range(no):     #Iteration using for loop
        print("Hello")

def DispalyIW(no):   #Iteration using while loop
    while no!=0:
        print("Hello")
        no=no-1

def DispalyR(no):   #Recursion function :calling function to function
    if no!=0:
        no=no-1
        print("Hello")
        DispalyR(no)    #recursive callable

def main():
    print("Enter the number of iterations")
    value=int(input())
    
    print("Calling iterative function using for loop")
    DispalyIF(value)
    print("Calling iterative function using while loop")
    DispalyIW(value)
    print("Calling Recursion function")
    DispalyR(value)
    
if __name__=="__main__":
    main()
    