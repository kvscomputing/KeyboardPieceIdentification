import pandas as pd
import numpy as np
import os
import csv

training_data = []
testing_data = []
validation_data = []
path = r"C:\Users\karthik\Downloads\GOOD_SPLITS\SPLITS"
arr_txt = [x for x in os.listdir(path) if x.endswith(".csv")]

counter = 0
for x in arr_txt:
    file = open(path + "\\" + str(x))
    reader = csv.reader(file)
    composer = str(next(reader))
    df = pd.read_csv(file)
    arr = df.to_numpy()
    neuron = 0
    if composer=="['Bach']":
        neuron = 0
    if composer=="['Beethoven']":
        neuron = 1
    if composer=="['Chopin']":
        neuron = 2
    if composer=="['Debussy']":
        neuron = 3
    if composer=="['Haydn']":
        neuron = 4

    if (counter % 10 == 8):
        validation_data.append((arr, neuron))
    if (counter % 10 == 9):
        testing_data.append((arr, neuron))
    else:
        training_data.append((arr, neuron))
    counter += 1




