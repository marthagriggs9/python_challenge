#module 3 challenge
#Find the total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote

#First I will need to import the operating system and import the csv
import csv
import os

#I need to create a dynamic path to the external files that will function across different operating systems
PyPollpath = os.path.join(r'C:/Users/Martha/GitHubClones/python_challenge/PyPoll/Resources/election_data.csv') 


#Define variables for all the information that needs to be included in the new file
#Total vote counter
total_votes_cast = 0
#Candidate options and candidate votes
candidate_options = []
#Empty dictionary for candidate votes
total_votes_per_candidate = {}
#Percentage of votes each candidate won
vote_percentage = 0
#Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0


#Open the csv file
with open(PyPollpath) as csvfile:
    #read the file object with the reader funciton
    csvreader = csv.reader(csvfile)
    #csv reader will need to skip the header row first
    csvheader = next(csvreader)
    
    #Find total number of cast votes
        
    total_votes_cast = len(list(csvreader))
        
        #Print candidate name from each row
    for row in csvreader:
            
        candidate_name = row[2]
        
        #If candidate does not match an existing candidate... 
    if candidate_name not in candidate_options:
            #Add the candidate name to the candidate list.
        candidate_options.append(candidate_name)
            
            #Begin tracking candidate vote count
        total_votes_per_candidate[candidate_name] = 0
            
            #Add a vote to that candidates count
        total_votes_per_candidate[candidate_name] += 1
            
       
#Print final vote count to the terminal
    election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes_cast:,}\n"
            f"-------------------------\n")
    print(election_results)