"""
Gavin Mok
"""
import string
import sys
from Bio import SeqIO


def main():
    counter = 0
    counter2 = 1
    kmer = []
    kmerdict = {}
    outputfile = open("kmers.txt", 'w')
    #setting up variables
    
    filename = sys.argv[1]
    fileformat = sys.argv[3]
    try:
        size = int(sys.argv[2])
    except ValueError:
        print("Entered size is not an integer")
        sys.exit()
    #getting command line inputs and validating size
    try:
        file = open(filename)
    except IOError:
        print("File not accessible")
        sys.exit()
    #testing if the file exists
    if (fileformat!='fastq') and (fileformat!='fasta'):
        print('Invalid format entered')
    #checking if valid format
    else:
        print("Counting kmers...")
        seqfile = open(filename, 'r')
        seqfiledna = SeqIO.parse(seqfile,fileformat)
        for record in seqfiledna:
            dnalist=list(record.seq)
            while size <= len(dnalist):
                while counter < size:
                    kmer.append(dnalist[counter])
                    counter += 1
                counter = counter2
                counter2 += 1
                size += 1
                #loop for creating kmers
                if str(kmer) not in kmerdict:
                    kmerdict[str(kmer)] = 1
                if str(kmer) in kmerdict:
                    kmerdict[str(kmer)] = kmerdict.get(str(kmer)) + 1
                #checking if kmer already exists
                kmer = []
            counter2 = 1
            counter = 0
            #place holders for specific kmer positions
            size = int(sys.argv[2])
            #reseting variables for next loop
        for kmer2 in kmerdict:
            kmer3 = kmerdict.get(str(kmer2))
            outputfile.write(str(kmer2)+'\t'+ str(kmer3) +'\n')
            #writing data to file
        print('Kmer data has been entered into kmers.txt')
main()
