#Total number of votes cast
#A complete list of candidates who received votes
#Total number of votes each candidate received
#Percentage of votes each candidate won
#The winner of the election based on popular vote

import csv
import os
#Assign a variable for the file to load
file_to_load = os.path.join("Resources","election_results.csv")
#Create filename 
file_to_save = os.path.join("Analysis", "election_analysis.txt")

#Initializations
total_votes = int()
total_votes = 0


#Candidate Options
candidate_options = []


#Open the results & Read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    #Read the header row
    headers = next(file_reader)

    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
        
        
print(candidate_options)



#using the open funtion with the "w" mode we will write data to the file
with open(file_to_save,"w") as txt_file:
    txt_file.write("Counties in the Election\n")
    txt_file.write("----------------------------\n")
    txt_file.write("Arapahoe\n")
    txt_file.write("Denver\n")
    txt_file.write("Jefferson\n")