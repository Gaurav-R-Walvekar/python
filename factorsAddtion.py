#  Problem statement : Accept number from user and return the addtion of factors of that no.
#   Input : 12         Output :   1  +  2  + 3  + 4 +6	=	16

def factors(no):
    print("factors of {}".format(no))
    sum=0
    
    for i in range(1,no):
        if no%i==0:
            print(i)
            sum=sum + i
    return sum
    
def main():
    print("Enter the first number")
    value1=int(input())
    
    iret=factors(value1)
    print("Addtion of factors is:",iret)
    
if __name__=="__main__":
    main()