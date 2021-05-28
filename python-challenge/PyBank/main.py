#import modeules
import os
import csv

#define resource file path
csvpath = os.path.join("Resources","budget_data.csv")

#declair variables
total_months = 0
total_net = 0
avg_net = 0.00
greatest_increase_amt = 0
greatest_increase_mo = ""
greatest_decrease_amt = 0
greatest_decrease_mo = ""

#open resource file
with open(csvpath) as csvfile:
    #read resource file
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #skip header
    csv_header=next(csvreader)

    #loop through each row of the dataset
    for row in csvreader:
        #create running total to determin total months (add 1 for each row)
        total_months += 1
        #create running total of profit/loss, found in the second list item of the row
        total_net += float(row[1])
        #calculate the average profit/loss per month
        avg_net = round(total_net / total_months,2)
        #track the greatest profits and losses
        if int(row[1]) > greatest_increase_amt:
            greatest_increase_amt = int(row[1])
            greatest_increase_mo = row[0]
        if int(row[1]) < greatest_decrease_amt:
            greatest_decrease_amt = int(row[1])
            greatest_decrease_mo = row[0]

#print results to terminal
print("Financial Analysis")
print("------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_net}")
print(f"Average Change: ${avg_net}")
print(f"Greatest Increase in Profits: {greatest_increase_mo} (${greatest_increase_amt})")
print(f"Greatest Decrease in Profits: {greatest_decrease_mo} (${greatest_decrease_amt})")

#output results to a new txt file

#define output file path
output_path =os.path.join("analysis","Financial Analysis.txt")

#open output file in write mode
with open(output_path, "w") as output_file:
    #print results to output file
    output_file.write(f"Financial Analysis\n")
    output_file.write("------------------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${total_net}\n")
    output_file.write(f"Average Change: ${avg_net}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase_mo} (${greatest_increase_amt})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_mo} (${greatest_decrease_amt})\n")