# consolidates NTC positives from Trim CFX runs
# example usage: cd to folder && python3 ben10MAFA.py
# creates a text file with NTC positives

import csv
import os
from glob import glob
from pathlib import Path
from shutil import copyfile

directory = os.getcwd()

def per_csv(target):
    x = []  # Sample
    y = []  # Cq

    with open(target,'r') as csvfile:
        file = csv.reader(csvfile, delimiter = ',')
        # add ntc's and scores to their own lists
        for row in file:
            for value in row:
                if (value.startswith('NTC')):
                    x.append(row[5])
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
            f.write(k + ": " + v + "\n")



""" main """

f = open("ben10MAFA.txt", "x")

paths = Path(directory).glob('**/*.csv',)
for path in paths:
    per_csv(path)
