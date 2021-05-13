#pip install psutil

import os
import time
import psutil
from sys import *
import schedule
i=0

def ProcessDisplay(FolderName="Marvellous"):

    Data=[]
    global i
    if not os.path.exists(FolderName):
        os.mkdir(FolderName)   #use to create the folder

    File_path=os.path.join(FolderName,"Marvellous %s.log"%i)
    i+=1
    fd=open(File_path,"w")

    for proc in psutil.process_iter():
        value=proc.as_dict(attrs=["pid","name","username"])
        Data.append(value)

    for element in Data:
        fd.write("%s\n"%element)

def main():
    print("---------Marvellous Infosystems--------")
    print("Script title:"+argv[0])

    if ((argv[1] == "-u") or (argv[1] == "-U")):
        print("Usage:Application_Name Schude_Time Directory_Name")
        exit()

    if ((argv[1] == "-h") or (argv[1] == "-H")):
        print("Help:it is used to create log file of runing processing")
        exit()

    schedule.every(int(argv[1])).minutes.do(ProcessDisplay)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()
