from sys import *
import os
import hashlib
import smtplib

def CalculateChecksum(path,blocksize=1024):#calculate checksum of each file
    fd = open(path,'rb')
    hobj = hashlib.md5()

    buffer=fd.read(blocksize)
    while len(buffer)>0:
        hobj.update(buffer)
        buffer=fd.read(blocksize)
    
    fd.close()
    return hobj.hexdigest()#convert the checksum to hexadecimal
        
def DirectoryTraversal(path):   #travel the folder
    print("Contents of the directory are")
    
    files={}            #Dictorny to hold checksum and file name
    for Folder,Subfolder,Filename in os.walk(path):
        print("Directory name is :"+Folder)
        for sub in Subfolder:
            print("Subfolder "+Folder+" is "+sub)
        for file in Filename:
            print("File name is :"+file)
            actualpath=os.path.join(Folder,file)
            hash=CalculateChecksum(actualpath)
            
            if hash in files:   #that checksum is already present
                files[hash].append(actualpath)
            else:                   #ther is no such checksum
                files[hash]=[actualpath]
            
    return files#send to main() arr{}

def DeletedFile(copys):     #deleting duplicate files and make log
    print("List of files file are save in log.txt file")
    i=0
    icnt=0
    fd=open("log.txt",'w')#create log file to store delete file name or parh
    
    for result in copys:
        icnt=0
        for path in result:
            icnt+=1
            if icnt>=2:
                fd.write("%s\n"%path)
                i+=1
                os.remove(path)
    fd.close()
    
    print("Number of files file deleted:",i)
    #mail(fd)
   

def Displayfiles(files):    #check duplicate files and send to deleting
    
    copys=list(filter(lambda x:len(x)>1,files.values()))#list of list only more then 1 value will come
    #files=((a.txt,b.txt,c.txt),(data.txt),(hello.txt,demo.txt,c.txt),(marvellous.txt))
    
    #copys=((a.txt,b.txt,c.txt),(hello.txt,demo.txt,c.txt))

    if(len(copys)>0):
        print("there are duplicate  files")
        
        print("To Delete the file press :Y")
        print("Dont delete the file press :N")
        yes=str(input())
        
        if(yes == "Y")or(yes == "y"):
            DeletedFile(copys)
        
        if(yes =="N") or( yes == "n"):
            print("file not deleted")
            exit(0)
            
    else:
        print("there are no files file")
        return
    

def mail(fd):
    sender="from@gmail.com"
    receivers = ["to@gmail.com"]
    message="body"

    try:
        sobj=smtplib.SMTP("smpt.gmail.com",587)
        sobj.starttls()
        sobj.login("sender@gmail.com","password")
        sobj.sendmail(sender,receivers,message)
        sobj.quit()
        print("Successfully sent email")

    except Exception:
        print("Error: unable to send email")


def main():
    print("Directory travesal script")
    
    if(len(argv)!=2):
        print("Error:Invalid number of arguments")
        exit()
        
    if(argv[1]=="-h") or (argv[1]=="-H"):
        print("It is a Directory cleaner script")
        exit()
        
    if(argv[1]=="-u") or (argv[1]=="-U"):
        print("Usage:Provide the absolute path of the target director")
        exit()
        
    arr={}
    arr=DirectoryTraversal(argv[1])
    Displayfiles(arr)
    
    
if __name__=="__main__":
    main()
    