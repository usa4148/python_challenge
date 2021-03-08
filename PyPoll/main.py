#
# Dan Cusick
# Data Scienct Boot Camp
# python-challenge PyPoll
#
#
#
import os
import csv
import numpy

csvpath = os.path.join('.', 'Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    #print(f"Header: {csv_header}")

    #num_votes = sum(1 for row in csvfile)
    #print(csvreader.line_num)
    #print("num_votes", num_votes)

    candidates = {}

    for vote in csvreader:
        if  vote[2] in candidates:                #candidates.get(vote[2]) != None:
            candidates[vote[2]] += 1
        else:
            candidates[vote[2]] = 1
            #print(f"{vote[2]}")



print("\nElection Results","\n-----------------------------")
print("Total Votes:", (csvreader.line_num - 1),"\n-----------------------------")
#print(" Total Votes:", num_votes,"\n-----------------------------")
#print(" Winner: ", pnl_total,"\n-----------------------------")
#print(f"{candidates}")
for x in candidates:
    print(x,": ", candidates[x])
