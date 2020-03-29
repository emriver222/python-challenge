# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
import csv

Month_count = 0
Net_Total = 0
ChangesList = []

csvpath = os.path.join('../../..','Bootcamp Files (Clone)','UofM-STP-DATA-PT-03-2020-U-C','02-Homework','03-Python','Instructions','PyBank','Resources','budget_data.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")



    # Read each row of data after the header
    FirstRow = next(csv_header)
    PreviousPL = FirstRow[1]
    for row in csvreader:
        #print(row)
        Month_count +=1
        Net_Total = row[1] + Net_Total
        NetChange = row[1] - PreviousPL
        PreviousPL = row[1]
        ChangesList.append(NetChange)



#assigning column var

 


#Question 1 -  The total number of months included in the dataset
        
        
#Question 2 - The net total amount of "Profit/Losses" over the entire period, sum list function?
Net_Total = Profit/Loss.sum


for row in csvreader:
        print(row[1].sum)

#Question 3 - The average of the changes in "Profit/Losses" over the entire period
Avg= Profit/Loss.avg

#Question 4 - The greatest increase in profits (date and amount) over the entire period
Max = Profit/Loss.max

    for row in csvreader:
        print(max(row[1]))

# #Question 5 - The greatest decrease in losses (date and amount) over the entire period
Min = Profit/Loss.min



print(f"Total Months: {str(Count)}")
print(f"Total Profits/Loss: {str(Net_Total)}")
print(f"The Average Profits/Loss: {str(Avg)}")
print(f"Greatest Increase Profits/Loss: {str(Max)}")
print(f"Greatest Decrease Profits/Loss: {str(Min)}")
