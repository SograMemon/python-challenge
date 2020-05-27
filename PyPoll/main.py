import os
import csv

csvpath = os.path.join("Resources","election_data.csv")

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    myheaders= next(csvreader)
    print(f"My Headers: {myheaders}")
    voteN=0
    for row in csvreader:
        voteN += 1
        #print(row)
    
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {voteN}")
    print("-------------------------")
    print("-------------------------")
    print("-------------------------")
    