"""
1.Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub()
for subtraction, Mult() for multiplication and Div() for division. All functions accepts two
parameters as number and perform the operation. Write on python program which call all the
functions from Arithmetic module by accepting the parameters from user.
"""
import Arithmetic


def main():
    print("enter the first number")
    no1=int(input())
    
    print("Enter the second number")
    no2=int(input())
    
    Arithmetic.Add(no1,no2)
    Arithmetic.Sub(no1,no2)
    Arithmetic.Mult(no1,no2)
    Arithmetic.Div(no1,no2)
    
if __name__=="__main__":
    main()