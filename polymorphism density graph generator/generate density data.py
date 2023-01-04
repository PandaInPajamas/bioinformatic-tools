"""
Gavin Mok
"""
#! /usr/bin/python
import string
import sys
from Bio import SeqIO
import re
import csv
#importing libraries

def main():
    file = open("plot.csv",'w',newline='')
    excelrow = csv.writer(file,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
    excelrow.writerow(["Position","Individual I","Individual C","Individual B","Individual A","Individual P","Individual D","Individual F","Individual E"])
    #initializing excel csv library and file
    
    print("Counting polymorphisms...")
    try:
        vcffile = sys.argv[1]
        readfile = open(vcffile,'r').readlines()
    except IOError:
        print("File not found")
        sys.exit()
    try:
        windsize = int(sys.argv[2])
    except ValueError:
        print("Window size must be an integer")
        sys.exit()
    incrementvalue = int(sys.argv[3])
    if incrementvalue > windsize:
        print("Increment value is larger than window size")
        sys.exit() 
    #testing variables
    
    windbeg = 0
    #beggining of window
    windfin = windsize
    #when window finishes
    i = []
    c = []
    b = []
    a = []
    p = []
    d = []
    f = []
    e = []
    ilist = []
    clist = []
    blist = []
    alist = []
    plist = []
    dlist = []
    flist = []
    elist = []
    individuallist = [i,c,b,a,p,d,f,e]
    length = len(readfile)-1
    position = str("")
    #initializing length of the file, individual lists and variables
    
    for line in readfile:
        start=re.search(r'^[chr02]+', line)
        if start:
            linedata = re.split(r'\s+', line)
            position=int(linedata[1])
            ilist = linedata[9]
            clist = linedata[10]
            blist = linedata[11]
            alist = linedata[12]
            plist = linedata[13]
            dlist = linedata[14]
            flist = linedata[15]
            elist = linedata[16]
            totallist = [ilist,clist,blist,alist,plist,dlist,flist,elist]
            if line == readfile[length]:
                endposition = position
        #storing data from read file into lists and setting final position
            
            for individual in range(len(totallist)):
                polymorph = re.search(r'^[1/1]+',totallist[individual])
                if polymorph:
                    individuallist[individual].append(position)
            #checking for polymorphisms in lists
            
    while windbeg <= endposition:
        excelcount = [windbeg,0,0,0,0,0,0,0,0]
        for person in range(len(individuallist)):
            for pos in individuallist[person]:
                if pos >= windbeg and pos < windfin:
                    excelcount[person+1] += 1
        excelrow.writerow(excelcount)
        windbeg += incrementvalue
        windfin = windbeg+windsize
    print("Data is saved to plot.csv")
    #counting polymorphisms and entering the count into excel
    
main()
#run program
