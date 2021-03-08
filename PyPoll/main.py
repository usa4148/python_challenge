#
# Dan C.
# Data Scienct Boot Camp
# python-challenge PyPoll
#

import os
import csv

# Open the text file for write
pypoll = os.path.join('.','analysis', 'PyPoll.txt')
pypollwriter = open(pypoll,'w')

# Open the csv file with the votes
csvpath = os.path.join('.', 'Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)

    # Create a dict for the tabulation
    candidates = {}

    for vote in csvreader:
        if  vote[2] in candidates:   # We already have the candidate in the dict, increment
            candidates[vote[2]] += 1
        else:
            candidates[vote[2]] = 1  # We do not yet have the candidate in the dict - add him and 1 vote
            

# Assuming no undercount the total number of votes is the number of rows less the header
total_v = csvreader.line_num - 1

# Print to the console
print("\nElection Results","\n-----------------------------")
print("Total Votes:", (total_v),"\n-----------------------------")
for x in candidates:
    print(x,": ", "{:.3f}%".format(candidates[x] / total_v * 100), candidates[x])
winner = max(candidates, key=candidates.get)
print("-----------------------------")
print("Winner: ", winner,"\n-----------------------------")

# Print to the txt file
print("\nElection Results","\n-----------------------------", file = pypollwriter)
print("Total Votes:", (total_v),"\n-----------------------------", file = pypollwriter)
for x in candidates:
    print(x,": ", "{:.3f}%".format(candidates[x] / total_v * 100), candidates[x], file = pypollwriter)
print("-----------------------------", file = pypollwriter)
print("Winner: ", winner,"\n-----------------------------", file = pypollwriter)

# The End