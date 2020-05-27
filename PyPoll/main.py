import os
import csv

csvpath = os.path.join("Resources","election_data.csv")

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    myheaders= next(csvreader)
    print(f"My Headers: {myheaders}")
    for row in csvreader:
        print(row)