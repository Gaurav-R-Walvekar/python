#  Problem statement : Accept number from user and display factors of that number.
#  Input : 12         Output :   1    2   3   4   6

def factors(no):
    print("factors of {}".format(no))
    for i in range(1,no):
        if no%i==0:
            print(i)


def main():
    print("Enter the first number")
    value1=int(input())
    factors(value1)

if __name__=="__main__":
    main()