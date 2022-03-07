#The data we need to retrieve
#1. The total number of votes cas
#2. A complete list of the candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote

import csv
import os

# Open the election results and read the file
#Assign a variable for the file to load and the path
fileToLoad = os.path.join("Resources", "election_reuslts.csv")
# Open th eelction results and read the file
with open(fileToLoad) as election_data:
    print(election_data)