print("Hello World/n")

#counties = ["Arapahoe", "Denver", "Jefferson"]
#if counties[3] != "Jefferson" :
#    print(counties[2])

#temperature = int(input("What is the temperature outside? "))

#if temperature > 80 :
#    print("Turn on the AC.")
#else:
#    print("Open the Windows.")

# What is the score?
#score = int(input("What is your test score? "))

# Determine the grade.
#if score >= 90:
#    print('Your grade is an A.')
#elif score >= 80:
#    print('Your grade is a B.')
#elif score >= 70:
#    print('Your grade is a C.')
#elif score >= 60:
#    print('Your grade is a D.')
#else:
#    print('Your grade is an F.')

import datetime

now = datetime.datetime.now()
print("The current time is ",now)


import csv
#open files
file_to_load = 'Resources/election_results.csv'
election_data = open(file_to_load,"r")

#Do Stuff

#close files
election_data.close()

#open files & do stuff
with open(file_to_load) as election_data:
    print(election_data)

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    #print(county + " county has " + str(voters) + " registered voters.")
    print(f"{county} county has {voters:,} registered voters.")

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")



