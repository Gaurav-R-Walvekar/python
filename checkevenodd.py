#Problem statement : Accept number from user and check whether the
#number is even or odd.

def check(no):
    if no%2==0:
        return True
    else:
        return False

def main():
    print("Enter the number to check:")
    no=int(input())
    
    iret=check(no)
    if iret==True:
        print("{} is Even:".format(no))
    else:
        print("{} is Odd:".format(no))
    

if __name__=="__main__":
	main()