import matplotlib.pyplot as plt
import pandas as pd
# import sys

testsperformed = []
months = []
dict = {}
keys = dict.keys()
values = dict.values()

# f = open(sys[1], 'r')
f = open('NTC Positives 2022.txt', 'r')
for row in f:
    row = row.split(' ')
    testsperformed.append(row[1])
    for element in testsperformed:
        left_text = element.partition("\\")[0]
        months.append(left_text)
        testsperformed.remove(element)

for key in months:
    temp = []
    temp.append(months.count(key))
    for counts in temp:
        dict[key] = counts

plt.bar(keys, values, color = 'b', label = 'Occurrences')
plt.ylabel('Frequency', fontsize = 12)
plt.xlabel('Month', fontsize = 12)
plt.title('Frequency of NTC Positives by Month - 2022', fontsize = 20)
plt.legend()
plt.show()

plt.pie(values, labels = keys, colors = ['y','b','g','c','r','g'], startangle=90,
        shadow=True, radius=1.2, autopct = '%1.1f%%')
plt.show()
