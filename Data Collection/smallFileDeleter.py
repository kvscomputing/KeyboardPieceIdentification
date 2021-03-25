import os
import csv

path = input("Enter file path for your splits: ")
arr_txt = [x for x in os.listdir(path) if x.endswith(".csv")]
for x in arr_txt:
    file = open(path  + '\\' +str(x))
    reader = csv.reader(file)
    lines = sum(1 for row in reader)
    file.close()
    if(lines < int(input("Enter the row limit: "))):
        os.remove(x)
