#Dependencies
import csv
import os

#Assign a variable for the file to load
file_to_load = os.path.join("Resources","election_results.csv")
#Create filename 
file_to_save = os.path.join("Analysis", "election_analysis.txt")

#Initializations
total_votes = int()
total_votes = 0
###Candidate Options
candidate_options = []
###Candidate Tally
candidate_votes = {}
###Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

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
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

#using the open funtion with the "w" mode we will write data to the file
with open(file_to_save,"w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)

    for candidate in candidate_votes:
        votes = candidate_votes[candidate]  
        vote_percentage = (votes/total_votes) * 100
        candidate_results = (f"{candidate}: {vote_percentage:.2f}% ({votes:,})\n")
        
        print(candidate_results)
        txt_file.write(candidate_results)

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate
    
    winning_candidate_summary = (
        f"--------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.2f}%\n"
        f"--------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)