# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
import csv

csvpath = os.path.join('budget_data.csv')

#Var Assignments
Month_Count = 0
NetChange = 0
PreviousPL = 0
ProfitLoss = 0
MonthProfit = 0
NetChangeRunning = 0


#List Assignments
ChangesList = []
Month = []


with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # Loop through the data
    for row in csvreader:    
        Month_Count +=1
        ProfitLoss += int(row[1])
        Month.append(str(row[0]))

        if NetChange != 0:
            MonthProfit = int(row[1])
            NetChange = MonthProfit - NetChange
            ChangesList.append(NetChange)
            NetChange = int(row[1])
        elif NetChange == 0:
            NetChange = int(row[1])


    Month.pop(0)
    MaxIncreaseIndex = ChangesList.index(max(ChangesList))
    MaxDecreaseIndex = ChangesList.index(min(ChangesList))
    MaxIncreaseValue = (Month[int(MaxIncreaseIndex)],max(ChangesList))
    MaxDecreaseValue = (Month[int(MaxDecreaseIndex)],min(ChangesList))


print("Total Months: "+ str(Month_Count))
print("Total Profit: "+ str(ProfitLoss))
print("Month of Minimum Change: "+ str(MaxDecreaseValue))
print("Month of Max Change: "+ str(MaxIncreaseValue))
print("Avg Change: "+ str((sum(ChangesList))/((Month_Count)-1)))


f= open("output.txt", "a")
print("Total Months: "+ str(Month_Count), file=f)
print("Total Profit: "+ str(ProfitLoss), file=f)
print("Month of Minimum Change: "+ str(MaxDecreaseValue), file=f)
print("Month of Max Change: "+ str(MaxIncreaseValue), file=f)
print("Avg Change: "+ str((sum(ChangesList))/((Month_Count)-1)), file=f)
f.close()
