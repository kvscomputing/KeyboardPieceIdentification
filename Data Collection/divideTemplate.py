import csv
import os
path = input("Enter file path of your splits: ")
arr_txt = [x for x in os.listdir(path) if x.endswith(".csv")]
print(arr_txt)
factor = float(input("What would you like to divide by? "))
for x in arr_txt:
    outputName = "AA_"+x
    with open(x, 'r') as inp, open(outputName, 'w', newline='') as out:
        writer = csv.writer(out)
        reader = csv.reader(inp)
        writer.writerow(next(reader))
        for row in csv.reader(inp):
            writer.writerow((float(row[0])/factor, float(row[1])/factor, float(row[2])/factor, float(row[3])/factor))
            
arr_txt = [x for x in os.listdir(path) if not(x.startswith("AA"))]
for x in arr_txt:
    os.remove(x)
