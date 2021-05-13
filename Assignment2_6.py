"""
6. Write a program which accept one number and display below pattern.
Input : 5
Output :
* * * * *
* * * *
* * *
* *
*
"""
def main():

    print("Enter the No:")
    no=int(input())
    k=no
    for i in range(no):
        for j in range(k):
            print("*",end=' ')
            
        print(" ")
        k=k-1

if __name__=="__main__":
    main()