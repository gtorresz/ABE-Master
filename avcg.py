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


    filesToProcess  = glob.glob("keygen10cgw15.csv", )
    filesToProcess += glob.glob("keygen20cgw15.csv", )
    filesToProcess += glob.glob("keygen30cgw15.csv", )
    filesToProcess += glob.glob("keygen40cgw15.csv", )
    filesToProcess += glob.glob("keygen50cgw15.csv", )
    filesToProcess += glob.glob("keygen60cgw15.csv", )
    filesToProcess += glob.glob("keygen70cgw15.csv", )
    filesToProcess += glob.glob("keygen80cgw15.csv", )
    filesToProcess += glob.glob("keygen90cgw15.csv", )
    filesToProcess += glob.glob("keygen100cgw15.csv", )
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
    filesToProcess  = glob.glob("enc10cgw15.csv", )
    filesToProcess += glob.glob("enc20cgw15.csv", )
    filesToProcess += glob.glob("enc30cgw15.csv", )
    filesToProcess += glob.glob("enc40cgw15.csv", )
    filesToProcess += glob.glob("enc50cgw15.csv", )
    filesToProcess += glob.glob("enc60cgw15.csv", )
    filesToProcess += glob.glob("enc70cgw15.csv", )
    filesToProcess += glob.glob("enc80cgw15.csv", )
    filesToProcess += glob.glob("enc90cgw15.csv", )
    filesToProcess += glob.glob("enc100cgw15.csv", )
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
    filesToProcess  = glob.glob("dec10cgw15.csv", )
    filesToProcess += glob.glob("dec20cgw15.csv", )
    filesToProcess += glob.glob("dec30cgw15.csv", )
    filesToProcess += glob.glob("dec40cgw15.csv", )
    filesToProcess += glob.glob("dec50cgw15.csv", )
    filesToProcess += glob.glob("dec60cgw15.csv", )
    filesToProcess += glob.glob("dec70cgw15.csv", )
    filesToProcess += glob.glob("dec80cgw15.csv", )
    filesToProcess += glob.glob("dec90cgw15.csv", )
    filesToProcess += glob.glob("dec100cgw15.csv", )
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


    f = open("averageKeygen-cgw15.csv","w")
    counter = 1;
    for each in avk:
        f.write(str(counter*10) + ":\t" + str(each/1000) + "\n")
        counter += 1
   
    f = open("averageEnc-cgw15.csv","w")
    counter = 1;
    for each in ave:
        f.write(str(counter*10) + ":\t" + str(each/1000) + "\n")
        counter += 1
    f = open("averageDec-cgw15.csv","w")
    counter = 1;
    for each in avd:
        f.write(str(counter*10) + ":\t" + str(each/1000) + "\n")
        counter += 1

    return 0


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:]))

