# consolidates NTC positives from Trim CFX runs

import csv
import os
from glob import glob
from pathlib import Path

directory = os.getcwd()
paths = Path(directory).glob('**/*.txt',)

def per_csv(target):
    x = []  # file name
    y = []  # Cq

    with open(target,'r') as csvfile:
        file = csv.reader(csvfile, delimiter = ',')
        # add ntc's and scores to their own lists
        for row in file:
            for value in row:
                if (value.startswith('NTC')):
                    x.append(target)
                    #csvfile.read()    if paths = '**/*.csv'
                    y.append(row[7])

    # combine the two lists into a dictionary
    mydict = {}
    for key in x:
        for value in y:
            mydict[key] = value
            y.remove(value)
            break

    # append to output file
    f = open("ben10MAFA.txt", "a")

    # write ntc positives to output stream
    for k, v in mydict.items():
        if (float(v) > 0):
            f.write(str(k) + ": " + str(v) + "\n")
            print(str(k) + ": " + str(v) + "\n")

""" main """

f = open("ben10MAFA.txt", "x")

for path in paths:
    per_csv(path)
