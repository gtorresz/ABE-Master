from __future__ import division 
import csv 
import sys 
from collections import defaultdict 
import glob

def main():
    avk = []
    ave = []
    avd = []
    count = 0
    for i in range(0,10):
        avk.append(0)
        ave.append(0)
        avd.append(0)


    filesToProcess  = glob.glob("keygen10ac17.csv", )
    filesToProcess += glob.glob("keygen20ac17.csv", )
    filesToProcess += glob.glob("keygen30ac17.csv", )

    print (filesToProcess)
    for filename in filesToProcess:
        print("Trying :" + filename)
        with open(filename, 'r') as csvh:
            dialect = csv.Sniffer().has_header(csvh.read(1024))
            csvh.seek(0)
            reader = csv.DictReader(csvh, dialect=dialect)
            for row in reader: 
                avk[count] += float(row['time(sec)'])
        count += 1
    count = 0
    filesToProcess  = glob.glob("enc10ac17.csv", )
    filesToProcess += glob.glob("enc20ac17.csv", )
    filesToProcess += glob.glob("enc30ac17.csv", )

    print (filesToProcess)
    for filename in filesToProcess:
        print("Trying :" + filename)
        with open(filename, 'r') as csvh:
            dialect = csv.Sniffer().has_header(csvh.read(1024))
            csvh.seek(0)
            reader = csv.DictReader(csvh, dialect=dialect)
            for row in reader: 
                ave[count] += float(row['time(sec)'])
        count += 1

    count = 0
    filesToProcess  = glob.glob("dec10ac17.csv", )
    filesToProcess += glob.glob("dec20ac17.csv", )
    filesToProcess += glob.glob("dec30ac17.csv", )

    print (filesToProcess)
    for filename in filesToProcess:
        print("Trying :" + filename)
        with open(filename, 'r') as csvh:
            dialect = csv.Sniffer().has_header(csvh.read(1024))
            csvh.seek(0)
            reader = csv.DictReader(csvh, dialect=dialect)
            for row in reader: 
                avd[count] += float(row['time(sec)'])
        count += 1 


    f = open("averageKeygen-ac17.csv","w")
    counter = 1;
    for each in avk:
        f.write(str(counter*10) + ":\t" + str(each) + "\n")
        counter += 1
   
    f = open("averageEnc-ac17.csv","w")
    counter = 1;
    for each in ave:
        f.write(str(counter*10) + ":\t" + str(each) + "\n")
        counter += 1
    f = open("averageDec-ac17.csv","w")
    counter = 1;
    for each in avd:
        f.write(str(counter*10) + ":\t" + str(each) + "\n")
        counter += 1

    return 0


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:]))

