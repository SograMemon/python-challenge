import os
import csv

csvpath = os.path.join("Resources","election_data.csv")

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    myheaders= next(csvreader)
    #print(f"My Headers: {myheaders}")
    voteN=1
    rowOne= next(csvreader)
    #print(rowOne)
    candidates=[]
    candidates.append(rowOne[2])
    votesRecieved=[1]
    for row in csvreader:
        #if voteN < 10:
            voteN += 1
            #print(row)
            counter= 0
            for candidate in candidates:
                counter += 1
                if candidate == row[2]:
                    i= candidates.index(candidate)
                    votesRecieved[i] += 1
                    break
                elif counter == len(candidates):
                    #print("Counter "+str(counter))
                    #print("Len"+str(len(candidates)))
                    candidates.append(row[2])
                    votesRecieved.append(0)
                
        #print(str(voteN))
        
    
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {voteN}")
    print("-------------------------")
    winnerValue=1 
    for i in range(len(candidates)):
        print(f"{candidates[i]} : {round((votesRecieved[i]/ voteN)*100, 3)} % ({votesRecieved[i]})")
        if winnerValue < round((votesRecieved[i]/ voteN)*100,3):
            winnerValue = round((votesRecieved[i]/ voteN)*100,3)
            winnerName = candidates[i]
    print("-------------------------")
    print(f"Winner : {winnerName}")
    print("-------------------------")
    print()
    