"""
8. Write a program which accept one number and display below pattern.
Input : 5
Output : 1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""
def main():
    print("Enter the No:")
    no=int(input())
    k=1
    for i in range(no+1):
        for j in range(i):      #if taking i as range the do no+1 to complete the loop
            print(k,end=' ')
            k=k+1
        print(" ")
        k=1

if __name__=="__main__":
    main()