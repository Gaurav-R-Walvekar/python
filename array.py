#take array and give its addition

import array

def Addition(arr):
    sum=0
    for i in range(len(arr)):
        sum=sum+arr[i]
    return sum


def main():
    arr=array.array('i',[])
    size=int(input("Enter the size :"))

    print("Enter the element :")

    for i in range(size):
        arr.append(int(input()))

    print(arr)

    ret=Addition(arr)
    print("Addition is  :",ret)

if __name__=='__main__':
    main()