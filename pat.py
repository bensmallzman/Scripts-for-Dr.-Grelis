# example usage:    python3 pat.py rmdl.mdlab.com/xxxxxxx
# only tested on X-Tractor Gene Statistics pages

import sys
import pandas as pd
import openpyxl

url = sys.argv[1]

table = pd.read_html(url)[0]
table = table.drop(table.columns[0], axis=1)
table = table.rename({'Unnamed: 1_level_0': '', 'Unnamed: 2_level_0': ''}, axis=1)
table['', 'Equipment'] = table['', 'Equipment'].map(lambda x: x.rstrip('- NJH'))

# for col in table.columns:
#     print(col)
# print(table)

table.to_excel("pat.xlsx")
