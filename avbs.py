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


    filesToProcess  = glob.glob("keygen10bsw07.csv", )
    filesToProcess += glob.glob("keygen20bsw07.csv", )
    filesToProcess += glob.glob("keygen30bsw07.csv", )
    filesToProcess += glob.glob("keygen40bsw07.csv", )
    filesToProcess += glob.glob("keygen50bsw07.csv", )
    filesToProcess += glob.glob("keygen60bsw07.csv", )
    filesToProcess += glob.glob("keygen70bsw07.csv", )
    filesToProcess += glob.glob("keygen80bsw07.csv", )
    filesToProcess += glob.glob("keygen90bsw07.csv", )
    filesToProcess += glob.glob("keygen100bsw07.csv", )
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
    filesToProcess  = glob.glob("enc10bsw07.csv", )
    filesToProcess += glob.glob("enc20bsw07.csv", )
    filesToProcess += glob.glob("enc30bsw07.csv", )
    filesToProcess += glob.glob("enc40bsw07.csv", )
    filesToProcess += glob.glob("enc50bsw07.csv", )
    filesToProcess += glob.glob("enc60bsw07.csv", )
    filesToProcess += glob.glob("enc70bsw07.csv", )
    filesToProcess += glob.glob("enc80bsw07.csv", )
    filesToProcess += glob.glob("enc90bsw07.csv", )
    filesToProcess += glob.glob("enc100bsw07.csv", )
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
    filesToProcess  = glob.glob("dec10bsw07.csv", )
    filesToProcess += glob.glob("dec20bsw07.csv", )
    filesToProcess += glob.glob("dec30bsw07.csv", )
    filesToProcess += glob.glob("dec40bsw07.csv", )
    filesToProcess += glob.glob("dec50bsw07.csv", )
    filesToProcess += glob.glob("dec60bsw07.csv", )
    filesToProcess += glob.glob("dec70bsw07.csv", )
    filesToProcess += glob.glob("dec80bsw07.csv", )
    filesToProcess += glob.glob("dec90bsw07.csv", )
    filesToProcess += glob.glob("dec100bsw07.csv", )
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


    f = open("averageKeygen-bsw07.csv","w")
    counter = 1;
    for each in avk:
        f.write(str(counter*10) + ":\t" + str(each/1000) + "\n")
        counter += 1
   
    f = open("averageEnc-bsw07.csv","w")
    counter = 1;
    for each in ave:
        f.write(str(counter*10) + ":\t" + str(each/1000) + "\n")
        counter += 1
    f = open("averageDec-bsw07.csv","w")
    counter = 1;
    for each in avd:
        f.write(str(counter*10) + ":\t" + str(each/1000) + "\n")
        counter += 1

    return 0


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:]))

