#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv

#read the csv file
csvpath = os.path.join(".", "Resources", "election_data.csv")
fhandle = open(csvpath, "r")
csvreader = csv.reader(fhandle, delimiter=",")
print(csvreader)

header = next(csvreader)
#print(f"csv header: {header}")

#open path for output txt file
output_path = os.path.join(".", "voter_output.txt")

#Establish variables
count = 0
poll = dict()
candidate_list = list()
name_list = list()
vote_list = list()
percent_list = list()


#isolate candidate list and determine vote counts
for line in csvreader:
    #print(line)
    candidate_name = line[2]
    candidate_list.append(candidate_name)
    count = count + 1


#print(candidate_list)
#print(count)

#Generate dictionary made up of candidate names and vote 
for i in candidate_list:
    poll[i] = poll.get(i,0) + 1

#print(poll)

#for k,v in poll.iems():
    #print(k,v)

    
#Isolate candidate name and vote count and add to seperate list()
tuples = poll.items()
#print(tuples)
for k,v in tuples:
    name_list.append(k)
    vote_list.append(v)
    
#print(name_list)
#print(vote_list)
winner = max(vote_list)
#print(winner)


#code for determining winner
winner = -1
winner_candidate = None
for k,v in tuples:
    if v > winner:
        winner = v
        winner_candidate = k
#print(winner)
#print(winner_candidate)


#code for vote percentages
for w in vote_list:
    percentage = (w/count * 100)
    percent_list.append(percentage)
    
#print(percent_list)

length = len(name_list)


#output path
output_file = open(output_path, 'w')

voter_output = (
            f"Election Results\n"
            f"-------------------------\n"
            f"Total Votes: {count}\n"
            f"-------------------------\n")
print(voter_output)
output_file.write(voter_output)
        
for j in range(length):
    voter_output_two = f"{name_list[j]}: {percent_list[j]:.3f}% ({vote_list[j]})\n"
    print(voter_output_two)
    output_file.write(voter_output_two)

voter_output_three = (
            f"-------------------------\n"
            f"Winner: {winner_candidate}\n"
            f"-------------------------\n")
print(voter_output_three)
output_file.write(voter_output_three)

