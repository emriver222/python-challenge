# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
import csv

csvpath = os.path.join('election_data.csv')


#Var Assignments
Vote_Count = 0

#List Assignments
CandList = []
CandDict = {}
CandDict2 = {}

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    for row in csvreader:
        VoterID = str(row[0])
        County = str(row[1])
        Candidate = str(row[2])
        Vote_Count +=1

        if Candidate not in CandList:
            CandList.append(Candidate)
            CandDict[Candidate] = 0
            CandDict2[Candidate] = 0
        CandDict[Candidate] += 1
        CandDict2[Candidate] += 1


        CandList.append(Candidate)


CandDict2 = (CandDict2[Candidate])/Vote_Count
CandListFinal = list(set(CandList))


max_value = max(CandDict.values())
max_keys = [k for k, v in CandDict.items() if v == max_value] 

FinaLen = len(CandListFinal)
KeyList = list(CandDict)


f= open("output.txt", "a")
print("Winner Is:" + str(max_keys), file=f)
print(CandListFinal, file=f)
print(CandDict, file=f)
print("Total Votes: "+str(Vote_Count), file=f)
print("Khan Percent of Votes:" + str(CandDict['Khan']/Vote_Count), file=f)
print("O' Tooley Percent of Votes:" + str(CandDict["O'Tooley"]/Vote_Count), file=f)
print("Li Percent of Votes:" + str(CandDict['Li']/Vote_Count), file=f)
print("Correy Percent of Votes:" + str(CandDict['Correy']/Vote_Count), file=f)
f.close()



print("Winner Is:" + str(max_keys))
print(CandListFinal)
print(CandDict)
print("Total Votes: "+str(Vote_Count))
print("Khan Percent of Votes:" + str(CandDict['Khan']/Vote_Count))
print("O' Tooley Percent of Votes:" + str(CandDict["O'Tooley"]/Vote_Count))
print("Li Percent of Votes:" + str(CandDict['Li']/Vote_Count))
print("Correy Percent of Votes:" + str(CandDict['Correy']/Vote_Count))