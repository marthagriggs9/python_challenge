# PyBank and PyPoll

**Module 3 challenge**

## PyBank

In this work, I created a Python script that analyzes the financial records of my company, PyBank.

I used the financial data found in [budget_data.csv](https://github.com/marthagriggs9/python_challenge/blob/main/PyBank/Resources/budget_data.csv) , which contained two columns: Date and Profit/Losses.

The Python script analyzed the records to find the following:

* The total number of months included in the dataset

* The net total amount of "Profit/Losses" over the entire period

* The changes in "Profit/Losses" over the entire period, and then the average of those changes

* The greatest increase in profits (date and amount) over the entire period

* The greatest decrease in profits (date and amount) over the entire period

## PyBank Results

```
Finacial Analysis
----------------------------
Total Months:  86
Total:  $22564198
Average Change: $-8311.11
Greatest Increase in Profits:  Aug-16  ($1862002)
Greatest Decrease in Losses:   Feb-14  ($-1825558)
```
## PyBank Code

I used the following code to count the number of rows in the data set (skipping the header row) to find the total number of months.

![image](https://user-images.githubusercontent.com/115905663/212436368-4c4e0be4-c87c-4407-bb06-66c29db20a09.png)

To find the net total amount of Profit/Losses, the code needed to loop through the rows and add up all the amounts in the Profit/Losses column (row 1). 

![image](https://user-images.githubusercontent.com/115905663/212436868-60f60bd5-7623-42f8-b02f-9b814a8b5d71.png)

Finding the average change in Profit/Losses over the entire period required looping through all the rows and subtracting the current months profit from the previous months profit and keeping track of those numbers in a list. Those values would need to be reset after each loop to get the new amount. Those profit changes would then need to be added together and divided by the number of months. However, one month would need to be subtracted from the total months given that the first month of the data set would not have a previous month to subtract from.

![image](https://user-images.githubusercontent.com/115905663/212437598-8b63f277-aa68-4542-a348-88581bce60b9.png)

Finally, I used the min and max functions to find the lowest and highest profit changes from the data set. I also used the index function to retrieve the given date that went with the lowest and highest profit change. 

![image](https://user-images.githubusercontent.com/115905663/212438086-f35b6e38-e7ea-4106-a38b-ae32dfb0a122.png)

This information was then printed to the terminal and exported to a text file. 

![image](https://user-images.githubusercontent.com/115905663/212438188-dfcddd14-dadb-4ed9-bf9f-fbc79d482ffe.png)


## PyPoll

In this work, I created a Python script for analyzing the votes of election results.

I used the poll data collected and stored in [election_data.csv](https://github.com/marthagriggs9/python_challenge/blob/main/PyPoll/Resources/election_data.csv), which was composed of three columns: Voter ID, County and Candidate.

The Python script analyzed the votes to find the following:

* The total number of votes cast

* A complete list of candidates who received votes

* The percentage of votes each candidate won

* The total number of votes each candidate won

* The winner of the election based on popular vote.

## PyPoll Results

```
Election Results
-------------------------
Total Votes: 369,711
-------------------------
Charles Casper Stockham: 23.0% (85,213)
Diana DeGette: 73.8% (272,892)
Raymon Anthony Doane: 3.1% (11,606)
-------------------------
Winner: Diana DeGette
-------------------------
```

## PyPoll Code

I used the following code to loop through the rows and add the total number of votes in the election.

![image](https://user-images.githubusercontent.com/115905663/212439198-eed76296-dde3-45a9-93da-f8fe37b87dae.png)

This was then printed to the terminal and exported to a text file.

![image](https://user-images.githubusercontent.com/115905663/212488203-caa4142d-3476-43be-b6b0-9d30b77f67eb.png)

I created a list to hold the names of the candidates that received votes in the election. The code looped through the candidate row and added the various names of the candidates to the list. 

![image](https://user-images.githubusercontent.com/115905663/212439344-481bd33a-8d1b-49fd-a2ee-23f913782999.png)

I also began tracking the candidate vote count to be held in a dictionary. This information would be used later to find the total number of votes that each candidate received, as well as who won the most votes (popular vote). 

![image](https://user-images.githubusercontent.com/115905663/212439584-262ac281-9163-4ad5-bf50-dcf088867feb.png)

To find the percentage of votes that each candidate received required dividing the total number of votes by the votes for each candidate (that was held in the dictionary) and multiplying the answer by 100. 

![image](https://user-images.githubusercontent.com/115905663/212440601-ec9a9dc9-d051-43d9-9b80-c40fc3417e80.png)

This information was then printed to the terminal and exported to the text file. 

![image](https://user-images.githubusercontent.com/115905663/212488302-9dce5b7e-2b7d-4ecd-92f3-66527fc6a9b6.png)

I needed to use the following code to determine the winning vote count and which candidate won the election. 

![image](https://user-images.githubusercontent.com/115905663/212488167-e2ae90be-fa19-49ef-abb5-43d045784475.png)

The winners name was then printed to the terminal and exported to the text file. 

![image](https://user-images.githubusercontent.com/115905663/212488342-585f076e-40ff-4660-b0bf-42114816f902.png)









