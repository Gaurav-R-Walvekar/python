
def AddtionF(data):#for loop
    sum=0
    for i in range(len(data)):
        sum=sum+data[i]
        
    return sum
    
def AddtionW(data):#while loop
    sum=0
    i=0
    while i<len(data):
        sum=sum+data[i]
        i=i+1
    return sum

i=0
sum=0
def AddtionR(data): #recursion
    global sum
    global i
    if i<len(data):
        sum=sum+data[i]
        i=i+1
        AddtionR(data)
        
    return sum

def main():
   arr=[]
   #print("Enter the size of array")
   size=int(input("Enter the size of array:"))
   
   for i in range(size):arr.append(int(input()))
      #OR  value=int(input())
      #    arr.append(value)
      #OR  arr.append(int(input())
    
   print("Data is:",arr)
    
   print("Addtion using For Loop:",AddtionF(arr))#direct call to function and return 
   print("Addtion using For while:",AddtionW(arr))
   print("Addtion using recursion :",AddtionR(arr))
   
   
if __name__=="__main__":
    main()
    