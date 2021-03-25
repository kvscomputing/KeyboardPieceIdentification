import csv
import os
composer = input("enter a composer + path: ")
just_name = input("enter composer: ")
name = [just_name]
path = input("Enter full path") + composer
arr_txt = [x for x in os.listdir(path) if x.endswith(".csv")]
print(arr_txt)
for x in arr_txt:
    outputName = "COM_"+x
    with open(x, 'r') as inp, open(outputName, 'w', newline='') as out:
        writer = csv.writer(out)
        writer.writerow(name)
        for row in csv.reader(inp):
            if str(row[2]) == " Note_on_c":
                writer.writerow((row[0],str(row[1])[1:], str(row[4])[1:], str(row[5])[1:]))
