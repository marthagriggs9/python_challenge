#module 3 challenege
#PyBank
#List of Tasks required for this challenge
#Find the total months included in the data set
#Find the net total amount of profit/losses over the entire period
#Find the changes in profit/losses over the entire period
    #Find the average of those changes
#Find the greatest increase in profits (date and amount) for the entire period
#Find the greatest decrease in profits (date and amount) for the entire period
#The results need to be printed to the terminal and exported to a text file


#First I will need to import the operating system and import the csv
import csv
import os

#I need to create a dynamic path to the external files that will function across different operating systems
PyBankpath = os.path.join("Resources", "budget_data.csv")

#Lists that will store the data from the csv file
months = []
profit_changes = []

#Define variables for all the information that needs to be included in the new file
countmonths = 0
netprofitloss = 0
previousmonthprofitloss = 0
currentmonthprofitloss = 0
profitlosschange = 0

#I need python to open the csv file
with open(PyBankpath, encoding= 'utf8') as csvfile:
    #csv reader will specify delimeter and variable to hold the contents 
        csvreader = csv.reader(csvfile, delimiter=",")
    #csv reader will need to skip the header row first
        csvheader = next(csvreader)
    
    
    
    
    #Read through each row of data after the header
        for row in csvreader:
            #Count the number of months
            countmonths += 1
            
            #Net total amount of the "Profit/Losses" over the entire period
            currentmonthprofitloss = int(row[1])
            netprofitloss += currentmonthprofitloss
            
            
            if (countmonths == 1):
                #Make the value of the previous month equal to the current month to keep track of changes
                previousmonthprofitloss = currentmonthprofitloss
                continue
            else:
                
                #Compute change in profit loss
                profitlosschange = currentmonthprofitloss - previousmonthprofitloss 
                
                #Append (add) each month to the months list 
                months.append(row[0])
                
                #Append (add) each profit loss change to the profit changes list
                profit_changes.append(profitlosschange)
                
                #Set the current month loss to the previous month loss for the next loop
                previousmonthprofitloss = currentmonthprofitloss
                
    #Find the sum of the changes in the Profit/Losses over the entire period
        sum_profitloss = sum(profit_changes)
    
    #Find the average of the changes in the Profit/Losses over the entire period and round it to the hundredths place
        average_profitloss = round(sum_profitloss/(countmonths - 1), 2)
        
    #Find the highest change in Profit/Losses over the entire period
        highest_change = max(profit_changes)
        
    #Find the lowest change in Profit/Losses over the entire period
        lowest_change = min(profit_changes)
        
    #Find the index value of the highest change in Profit/Losses over the entire period
        highest_month_index = profit_changes.index(highest_change)
        
    #Find the index value of the highest change in Profit/Losses over the entire period
        lowest_month_index = profit_changes.index(lowest_change)
        
    #Assign the best and worst month to the respective values
        best_month = months[highest_month_index]
        worst_month = months[lowest_month_index]
        
            
#Print the analysis summary to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {countmonths}")            
print(f"Total:  ${netprofitloss}") 
print(f"Average Change: ${average_profitloss}")
print(f"Greatest Increase in Profits:  {best_month}  (${highest_change})")
print(f"Greatest Decrease in Losses:   {worst_month}  (${lowest_change})")
           
            
            
#Set a variable for the output file that will contain the information that will be exported to the text file
output_file = os.path.join("analysis", "budget_data_final.txt")

#open the output file 
with open(output_file, "w") as datafile:
    
#Write out the analysis summary into the text file    
    datafile.write("Finacial Analysis\n")
    datafile.write("----------------------------\n")
    datafile.write(f"Total Months:  {countmonths}\n")
    datafile.write(f"Total:  ${netprofitloss}\n")
    datafile.write(f"Average Change: ${average_profitloss}\n")
    datafile.write(f"Greatest Increase in Profits:  {best_month}  (${highest_change})\n")
    datafile.write(f"Greatest Decrease in Losses:   {worst_month}  (${lowest_change})\n")
    
    
    
    