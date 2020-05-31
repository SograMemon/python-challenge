import os
import csv
from datetime import datetime

filepath = os.path.join("Resources","employee_data.csv")
outpath = os.path.join("Analysis", "employee_out_data.csv")
empId = []
date = []
ssn = []
firstName = []
lastName = []
stateAbri = ["Alabama" , "AL", "Alaska", "AK", "Arizona", "AZ", "Arkansas", "AR", "California", "CA","Colorado", "CO", "Connecticut", "CT" 
,"Delaware", "DE", "Florida", "FL", "Georgia", "GA","Hawaii", "HI", "Idaho", "ID", "Illinois", "IL", "Indiana", "IN", "Iowa", "IA", "Kansas", "KS", "Kentucky", "KY"
, "Louisiana", "LA", "Maine", "ME", "Maryland", "MD", "Massachusetts", "MA", "Michigan", "MI", "Minnesota", "MN", "Mississippi", "MS", "Missouri", "MO"
, "Montana", "MT", "Nebraska", "NE", "Nevada", "NV", "New Hampshire", "NH", "New Jersey", "NJ", "New Mexico", "NM", "New York", "NY", "North Carolina", "NC"
, "North Dakota", "ND", "Ohio", "OH", "Oklahoma", "OK", "Oregon", "OR", "Pennsylvania", "PA", "Rhode Island", "RI", "South Carolina", "SC", "South Dakota", "SD"
, "Tennessee", "TN", "Texas", "TX", "Utah", "UT", "Vermont", "VT", "Virginia", "VA", "Washington", "WA", "West Virginia", "WV", "Wisconsin", "WI", "Wyoming", "WY"]
abri= []
with open (filepath, 'r') as csvfile:
    csvreader= csv.reader(csvfile, delimiter=',')
    myheader = next(csvreader)
    for row in csvreader:
        empId.append(row[0])
        firstName.append(row[1].split(" ")[0])
        lastName.append(row[1].split(" ")[1])
        date_object =datetime.strptime(row[2], '%Y-%m-%d')
        date.append(date_object.strftime('%m/%d/%Y'))
        ssn_str = row[3]
        ssn.append(ssn_str.replace(ssn_str[0:7], "***-**-"))
        abriIndex=stateAbri.index(row[4])
        abri.append(stateAbri[abriIndex+1])

content = zip(empId, firstName, lastName, date, ssn, abri)

with open(outpath, 'w', newline="") as writefile:
    writer= csv.writer(writefile)
    writer.writerow(["Emp Id", "First Name", "Last Name", "DOB", "SSN", "State"])
    writer.writerows(content)
    
    
