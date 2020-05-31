import os
import csv

csvpath= os.path.join('Resources','budget_data.csv')

with open (csvpath) as file_handler:
    lines = csv.reader(file_handler, delimiter=',')
    myvariable=next(lines)
    
    
    greatestInc = greatestDec = next(lines)
    monthsN= 1
    total= int(greatestInc[1])
    
    for row in lines:
        monthsN += 1
        total += int(row[1])
        if int(greatestInc[1]) < int(row[1]) :
            greatestInc = row
        if int(greatestDec[1]) > int(row[1]):
            greatestDec = row

        #print(row)
    avg= total/monthsN
    print('Financial Analysis')
    print('----------------------------')
    print (f"Total Months: {monthsN}")
    print (f"Total: $ {total}")
    print(f"Average Change: $ {avg}")
    print(f"Greates Increase in profits: {greatestInc[0]} ($ {greatestInc[1]})")
    print(f"Greates Decrease in profits: {greatestDec[0]} ($ {greatestDec[1]})")
