# Election_Analysis
Using Python to make an analysis of an election

## Project Overview
The main objective of this project was to help an employee in charged of the Colorado election audit. Python and Visual Studio Code were used in order to help him to automate and obtain the results needed. The task to complete were to report:
1.	The total number of votes casts.
2.	The total number of votes for each candidate.
3.	The percentage of votes for each candidate.
4.	The winner of the election based on the popular vote. 

## Resources
-Data Source: election_results.csv 

-Software: Python 3.7.6, and Visual Studio Code 1.38.1

## Summary 
The analysis of the Colorado election showed that:

-There were **369,711** votes casts in the election

-Candidates’ names:
 1. Charles Casper Stockham 
 2. Diana DeGette
 3. Raymon Anthony Doane
 
-The results of each candidate were:
 * Charles Casper Stockham received **23.03%** of the votes and **85,213** votes
 * Diana DeGette received **73.8%** of the votes and **272,892** votes
 * Raymon Anthony Doane received **3.1%** of the votes and **11,606** votes
 
-The winner of the election was:
 * Diana DeGette, who received **73.8%** of the votes and **272,892** votes

## Challenge Overview
There was more information about the election audit that needed to be delivered. This data was related to the counties of Colorado. The new tasks were to report:
1.	The voter turnout for each county. 
2.	The percentage of votes from each county out of the total count.
3.	The county with the highest turnout. 

## Election Audit Summary 
The final analysis of the Colorado election showed that:

-There were **369,711** votes casts in the election

-The results of each county were:
 * Jefferson received **10.5%** of the votes and **38,855** votes
 * Denver received **82.8%** of the votes and **306,055** votes
 * Arapahoe received **6.7%** of the votes and **24,801** votes
 
-The county with the highest number of votes was:
 * Denver
 
-The results of each candidate were:
 * Charles Casper Stockham received **23.03%** of the votes and **85,213** votes
 * Diana DeGette received **73.8%** of the votes and **272,892** votes
 * Raymon Anthony Doane received **3.1%** of the votes and **11,606** votes
 
-The winner of the election was:
 * Diana DeGette, who received **73.8%** of the votes and **272,892** votes
 
 <img width="246" alt="2" src="https://user-images.githubusercontent.com/111388644/192407805-364c7890-2b04-4e05-b680-baabade26a4f.png">

## Challenge Summary
This Python script can be modified using Visual Studio Code for further analyses. It could be used for another election analysis, and the only thing that would need to be changed is the *file_to_load*. Instead of writing the path to *”election_results.csv”*, the name of another file containing data of another election *(maybe the elections of a different state)*, would be written in its place. 

<img width="422" alt="1" src="https://user-images.githubusercontent.com/111388644/192407455-ace4a5ba-9c71-4a68-b396-22abb13186ce.png">

Another way this script could be modified to serve another election analysis would be to change the *if* statements, in case they would want to obtain the smallest county turnout or the candidate with less votes. The *greater than* signs would need to be modified. The name or the variables would need to be changed as well, for example: *Smallest_county_turnout* would replace *largest_county_turnout*.

<img width="529" alt="4" src="https://user-images.githubusercontent.com/111388644/192409845-a9eb0ba0-b222-4fa4-8b9a-266c7f1f0b1d.png">
