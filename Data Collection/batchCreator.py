from pathlib import Path
import time
import os


def convertFiles(path, composer):
    path = path + composer
    arr_txt = [x for x in os.listdir(path) if x.endswith(".mid")]
    print(arr_txt)
    for x in arr_txt:
        p = path + x[:-4]+".bat"
        myBat = open(p,'w+')
        c = input("Enter file path to Midicsv: ")+" "+x+" "+x[:-4]+".csv"
        myBat.write(c)
        myBat.close()

convertFiles(input("Enter full path A: "), input("Enter composer's folder path: "))
