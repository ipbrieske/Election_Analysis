# Election_Analysis

## Overview of Election Audit
	
The purpose of this project is to perform an analysis of election results among three Colorado counties. In order to perform this analysis, we were given a .csv file of all submitted votes with voter IDs, the County the vote was submitted in, and which candidate was selected by each voter. From this resource, we were able to leverage Python to automate creation of a summary document with relevant statitstics about the election. With this tool, we are able to identify with confidence the winner of the election. 

## Resources

VS Code
Python

## Election-Audit Results

![Image 1: Election Analysis.csv](

- Votes Cast

	- A total of 369,711 votes were cast in this election. This outcome was determined by taking the sum of all votes recorded in election_results.csv.

- Votes by County

	- Denver County: 82.8% of the vote with 306,055 total votes cast
	- Jefferson County: 10.5% of the vote with 38,855 total votes cast
	- Arapahoe County: 6.7% of the vote with 24,801 total votes cast

	- Denver County provided the most votes in the election

- Votes by Candidate
	
	- Diana DeGette received 73.8% of the vote with 272,892 total votes
	- Charles Casper Stockham received 23.0% of the vote with 85,213 total votes
	- Raymon Anthony Doane received 3.1% of the vote with 11,606 total votes

- Winner

	- Diana DeGette is the winner of this election, after receiving 73.8% of the vote and 272,892 votes in total

## Summary

This Python script has considerable utility beyond the scope of this project. Any .csv file formatted in the same way as the original can be analyzed by running this program with some further modifications. The program already retains the capability to dynamically read files with any number of candidates and counties. This would greatly reduce the workload of and the costs to the Election Commission in future elections. This code can also be modified - upon the contracting of our firm for futher work - to give a breakdown of candidate votes by county, as well as email the final analysis document to any relevant parties immediately upon completion. For further information please contact. 
