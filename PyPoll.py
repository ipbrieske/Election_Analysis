#The data we need to retrieve
#1. The total number of votes cas
#2. A complete list of the candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote

import csv
import os

# Create a file name variable to a direct or indirect path to the file
fileToLoad = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
fileToWrite = os.path.join("analysis", "election_results.txt")

# USing the open() function with the "w" mode we will write data to the file
with open(fileToLoad) as electionData:
    # To Do: read and analyze the data here
    fileReader = csv.reader(electionData)

    # Print Header row
    headers = next(fileReader)
    print(headers)
    