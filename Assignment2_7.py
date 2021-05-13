"""
7. Write a program which accept one number and display below pattern.
Input : 5
Output : 1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""
def main():
    print("Enter the No:")
    no=int(input())
    k=1
    for i in range(no):
        for j in range(no):
            print(k,end=' ')
            k=k+1
        print(" ")
        k=1

if __name__=="__main__":
    main()