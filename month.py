import csv
import sys
import os
from glob import glob
from pathlib import Path

directory = os.getcwd()
cqscores = []
contents = []
month = []
parent = []
x = []
# y = []

for item in os.walk(directory):
    try:
        dirnames = item[1]
        filenames = item[2]
        for foldername in dirnames:
            if (sys.argv[1] in foldername):
                paths = Path(foldername).glob('**/*.txt',)
                for path in paths:
                    month.append(path)
    except:
        pass

totalRuns = len(month)

# open each run for the month, separate rows
k = 0
for run in month:
    with open(run,'r') as csvfile:
        file = csv.reader(csvfile, delimiter = ',')
        for row in file:
            try:
                contents.append(row[4])
                cqscores.append(row[7])
                parent.append(month[k])
            except:
                pass
    k = k + 1

for p in parent:    
    for c in contents:
        for s in cqscores:
            if (s != 'nan') and (s != 'NaN') and (s != 'NAN') and (s != 'Cq'):
                try:
                    temp = float(s)
                    if ("NTC" in c) and (temp > 0):
                        x.append(p)
                        #y.append(temp)
                except:
                    pass
                    
res = [*set(x)]
statistic = "{:.0%}".format(len(res)/totalRuns)
print(sys.argv[1], "had", totalRuns, "total runs, and", len(res), "yielded positives, so the percentage of positive runs per total", sys.argv[1], "runs:", statistic)
try:
    f = open('monthly_rate.txt', 'x')
except:
    f = open('monthly_rate.txt', 'a')
    
f.write(sys.argv[1] + " had " + str(totalRuns) + " total runs, and " + str(len(res)) + " yielded positives, so the percentage of positive runs per total " + sys.argv[1] + " runs: " + statistic + "\n")
