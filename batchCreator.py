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
        c = "C:\\Users\\Kazuya\\Desktop\\midicsv-1.1\\Midicsv.exe "+x+" "+x[:-4]+".csv"
        myBat.write(c)
        myBat.close()

convertFiles(input("Enter full path"), input("Enter composer's specific folder path: "))
