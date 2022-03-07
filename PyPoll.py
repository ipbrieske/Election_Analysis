#The data we need to retrieve
#1. The total number of votes cas
#2. A complete list of the candidate who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote

import csv
import os

# Create a file name variable to a direct or indirect path to the file
fileToLoad = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
fileToSave = os.path.join("analysis", "election_results.txt")

totalVotes = 0
candidates = []
candidateVotes = {}
# USing the open() function with the "w" mode we will write data to the file
with open(fileToLoad) as electionData:
    # To Do: read and analyze the data here
    fileReader = csv.reader(electionData)

    # Print Header row
    headers = next(fileReader)

    # Cycle through all the rows and collect data
    for row in fileReader:
        # 2. Add to the total vote count
        totalVotes += 1
        candidateName = row[2]

        if candidateName not in candidateVotes:
            #add the candidate name to the candidate list
            candidates.append(candidateName)
            #Begin tracking that candidate vote count
            candidateVotes[candidateName] = 0
        candidateVotes[candidateName] += 1


# Winning Candidate and Winning Count Tracker
winningCandidate = ""
winningCount = 0
winningPercentage = 0

# 3. Print the total votes
print(totalVotes)
print(candidates)
print(candidateVotes)


for candidateName in candidates:
    votes = candidateVotes[candidateName]

    votePercentage = float(votes) / float(totalVotes) * 100

    print(f"{candidateName}: received {votePercentage:.2f}% of the vote.")
    # Determine winning vote count and candidate
    # 1. Determine if the votes are greater than the winning count.
    if (votes > winningCount) and (votePercentage > winningPercentage): 
        # 2. If true then set winningCount = votes and winningPercent = votePercentage
        #vote percentage
        winningCount = votes
        winningPercentage = votePercentage
        # 3. Set the winningCandidate equal to the candidate's name
        winningCandidate = candidateName

    #votes to the terminal
    print(f"{candidateName}: {votePercentage:.1f}% ({votes:,})\n")

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winningCandidate}\n"
    f"Winning Vote Count: {winningCount:,}\n"
    f"Winning Percentage: {winningPercentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
