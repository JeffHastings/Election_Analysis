#The Data we need to retrieve.
#1. Total number of votes cast
#2. A complete list of candidates who received votes
#3. Total number of votes each candidate received
#4. Percentage of votes each candidate won
#5. The winner of the election based on populare votes

#Add our dependencies
import csv
import os
#Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
#Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis","election_analysis.txt")

#Initialize a total vote counter
total_votes = 0.0

#Candidate Options and candidate votes
candidate_options = []

#Declare empty dictionary
candidate_votes = {}

#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Read the header row
    headers = next(file_reader)

    #Print each row in the CSV file.
    for row in file_reader:
        #Add to the total vote count.
        total_votes+=1
        
        #Print the candidate name for each row
        candidate_name = row[2]

        if candidate_name not in candidate_options: 
            #Add it to the list of candidates.
            candidate_options.append(candidate_name)

            #Begin tracking that candidates vote count.
            candidate_votes[candidate_name] = 0

        #Add to that candidates vote count.
        candidate_votes[candidate_name] += 1

    #Determine the percentage of votes for each candidate by looping through the data
     #Iterate through the candidate list
        for candidate in candidate_votes:

            #Retrieve the vote count of a candidate.
            votes = candidate_votes[candidate]

            #Calculate the percentage of votes.
            vote_percentage = float(votes)/ float(total_votes) *100

            # To do:Print out each candidates name, vote count, and percentage of votes to the terminal
            print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
            
            #Determine if the votes are greater than the winning count
            if(votes > winning_count) and (vote_percentage > winning_percentage):

                #If true then set winning_count = votes and winning_percent = vote_percentage
                winning_count = votes
                winning_candidate = candidate
                winning_percentage = vote_percentage
 
                #set the winning candidate equal to the candidates name
                winning_candidate_summary = (
                    f"-----------------------------\n"
                    f"Winner: {winning_candidate}\n"
                    f"Winning Vote Count:{winning_count:,}\n"
                    f"Winning Percentage: {winning_percentage:.1f}%\n"
                    f"------------------------------\n")
                print(winning_candidate_summary)

                
            #print the candidate name and percentage of votes.
            #print(f"{candidate} received {vote_percentage:.1f}% of the vote.")
     
#Print the candidate vote dictionary
#print(candidate_votes) 



    


    #Print the file object.
    #print(election_data)


#Using the open() function with the "w" mode we will write data to the file
#open(file_to_save,"w")

#Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis","election_analysis.txt")

#Using the with statement open the file as a text file.
#with open(file_to_save, "w")as txt_file:
    # Write three counties to the file.
    #txt_file.write("Counties in the Election\n--------------------------\nArapahoe\nDenver\nJefferson")
