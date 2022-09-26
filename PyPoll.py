# The data we need to retrieve.
# 1. The total number of votes casts.
# 2. A complete list of candidates who received votes.
# 3. Total number of votes each candidate received.
# 4. Percentage of votes each candidate won. 
# 5. The winner of the election based on popular vote. Resources\election_results.cvs

# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'

# Open the election results and read the file.


# Import csv and os modules
import csv
import os

# Assign a variable for the file to load from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Add the accumulator (initialize a total vote counter)
total_votes = 0


# 2. Declare a new list
candidate_options = []


#Declare an empty dictionary
candidates_votes = {}


# Declare variables for winning candidate, count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:


#To do: read and analyze the data here.

# Read the file object with the reader function.
    file_reader = csv.reader(election_data)

# Print the header row.
    headers = next(file_reader)
    

# Start the for loop using row variable to get the total number of votes.
    for row in file_reader:
        # Increment the total_votes by 1 (add total vote count)
        total_votes = total_votes + 1

        #Continue in the same loop to get the candidates in the election
        candidate_name = row[2]

        # If statement
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            #Create each candidate as a key
            candidates_votes[candidate_name] = 0

        candidates_votes[candidate_name] += 1

# Save the results to our text file.
file_to_save = os.path.join("Resources", "election_results")
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # For loop to iterate through canditates_options[]
    for candidate_name in candidates_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidates_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # 4. Print the candidate name and percentage of votes.
        #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
         # Adding each candidate's election results to the election_results.txt file
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

      


    #  To do: print out each candidate's name, vote count, and percentage of votes to the terminal.
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Determine if the votes are greater than the winning count (0).
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    

    # Print the winning candidate summary
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)


        # Print each candidate's name, their vote count, and their percentage of votes


    # 1.3. Print the total votes
    #print(total_votes)

    # Print the candidate in the election.
    #print(candidate_options)

    # Print the candidate vote dictionary.
    #print(candidates_votes)
