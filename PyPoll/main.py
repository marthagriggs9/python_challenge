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
#Assign a variable to load a file from a path
PyPollpath = os.path.join("Resources", "election_data.csv")
#Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")  



#Define variables for all the information that needs to be included in the new file
#Total vote counter
total_votes = 0
#Candidate options and candidate votes
candidate_options = []
#Empty dictionary for candidate votes
candidate_votes = {}
#Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the csv file
with open(PyPollpath) as csvfile:
    #read the file object with the reader funciton
    csvreader = csv.reader(csvfile, delimiter=',')
    #csv reader will need to skip the header row first
    csvheader = next(csvreader)
    
        #Find total number of cast votes
        #Print candidate name from each row
    for row in csvreader:
        total_votes += 1
            
        candidate_name = row[2]
        
        #If candidate does not match an existing candidate... 
        if candidate_name not in candidate_options:
            #Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
      
           #Begin tracking candidate vote count
            candidate_votes[candidate_name] = 0
            
        #Add a vote to that candidates count
        candidate_votes[candidate_name] += 1
            
#Save tje results to the text file.
with open(file_to_save, "w") as txt_file:
       
#Print final vote count to the terminal
    election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
    print(election_results, end="")
    #Save the final vote count to the text file
    txt_file.write(election_results)
            
     
    #Determine the percentage of votes for each candidate by looping through the counts
    #Iterate through the candidate list
    for candidate_name in candidate_votes:
        #Retrieve vote count of candidate
        votes = candidate_votes[candidate_name]
        #Calculate the percentage of votes
        vote_percentage = float(int(votes))/float(int(total_votes)) * 100
        #Print the candidate name and percentage of votes
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        print(candidate_results) 
        #Save the candidate results to the text file
        txt_file.write(candidate_results)
        
        #determine the winning vote count
        if(votes>winning_count):
            #If true then set the winning count to votes
            winning_count = votes
            #If true then set the winning candidate to the candidate name
            winning_candidate = candidate_name
            
            
            
    winning_candidate_summary = ( 
            f"-------------------------\n"                         
            f"Winner: {winning_candidate}\n"
            f"-------------------------\n")
        
    print(winning_candidate_summary)
        
    txt_file.write(winning_candidate_summary)