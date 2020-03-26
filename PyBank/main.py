# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
import csv

csvpath = os.path.join('../../..','Bootcamp Files','UofM-STP-DATA-PT-03-2020-U-C','02-Homework','03-Python','Instructions','PyBank','Resources','budget_data.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)

#Counts the number of rows/months
with open(csvpath, newline='') as csvfile:
        row_count = sum(1 for row in csvfile)
        print (row_count)





    