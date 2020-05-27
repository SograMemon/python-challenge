import os
import csv

csvpath= os.path.join('Resources','budget_data.csv')

with open (csvpath) as file_handler:
    lines = csv.reader(file_handler, delimiter=',')
    myvariable=next(lines)
    print(f"These are my csv headrs: {myvariable}")
    for row in lines:
        print(row)
