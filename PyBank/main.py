import os
import csv

csvpath= os.path.join('Resources','budget_data.csv')
outputPath = os.path.join('Analysis','output_budget_data.txt')

with open (csvpath) as file_handler:
    lines = csv.reader(file_handler, delimiter=',')
    myvariable=next(lines)
    
    
    greatestInc = next(lines)
    greatestDec = greatestInc[:]
    temp = int(greatestInc[1])
    print()
    #print(greatestDec)
    #print(temp)
    totalChange = int(greatestInc[1])
    monthsN= 1
    total= int(greatestInc[1])
    
    for row in lines:
        monthsN += 1
        total += int(row[1])
        profit = int(row[1]) - temp
        totalChange += profit
        if int(greatestInc[1]) < profit :
            greatestInc[0] = row[0]
            greatestInc[1] = profit
        if int(greatestDec[1]) > profit:
            greatestDec[0] = row[0]
            greatestDec[1] = profit
            #print(greatestDec)
        temp = int(row[1])
        #print(temp)

        #print(row)
    avg= totalChange
 

writeTxtFile = open (outputPath, 'w')
writeTxtFile.write(f" Financial Analysis \n ---------------------------- \n Total Months: {monthsN} \n Total: $ {total} \n Average Change: $ {avg} \n Greatest Increase in profits: {greatestInc[0]} ($ {greatestInc[1]}) \n Greatest Decrease in profits: {greatestDec[0]} ($ {greatestDec[1]})")
writeTxtFile.close()

with open(outputPath, 'r') as txtfile:
    reader=txtfile.read()
    print(reader)

    
