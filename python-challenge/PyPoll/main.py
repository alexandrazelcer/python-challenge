#modules
import os
import csv

#set file path 
election_data_csv = os.path.join("Resources", 'election_data.csv')

# declare variables 
totalvotes = 0
candidates = []
cand_votes = []
cand_percent = []
winner = ""

#open csv
with open(election_data_csv, newline="") as csvfile:
    #read resource file
    csvreader = csv.reader(csvfile, delimiter = ",")
        
    #skip header row
    csv_header = next(csvreader)

    #loop through each row of the dataset
    for row in csvreader:
        # Add 1 to total vote-counter running total
        totalvotes += 1 

        #read in the candidate from column 3 of csv
        candidate_in = (row[2]) 

        #populate candidate list, add list slots for votes and percentages lists
                
        if candidate_in in candidates:
            candidate_index = candidates.index(candidate_in)
            cand_votes[candidate_index] = cand_votes[candidate_index] + 1
            
        else: 
            candidates.append(candidate_in)  
            cand_votes.append(1)    
pct = []
max_votes = cand_votes[0]
max_index = 0

# Add to running vote list total
for x in range(len(candidates)):

    vote_pct = round(cand_votes[x]/totalvotes*100, 2)
    pct.append(vote_pct)
    
    if cand_votes[x] > totalvotes:
        totalvotes = cand_votes[x]
        max_index = x


#find winner based on candidates list index that matches the index of the max value of the candidates' votes list
winner = candidates[cand_votes.index(max(cand_votes))]


# Displaying results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {totalvotes}")
print("--------------------------")
for x in range(len(candidates)):
    print(f'{candidates[x]}: {pct[x]}% ({cand_votes[x]})')
print("--------------------------")
print(f"Winner: {winner}")
print("--------------------------")

# Exporting to .txt file

#define output file path
output_path = os.path.join("Analysis", "Election Analysis.txt")

#open output file in write mode 
with open(output_path, "w", newline="") as output_file: 
    #print results to output file
    output_file.write("Election Results\n")
    output_file.write("---------------------------\n")
    output_file.write(f"Total Votes: {totalvotes}\n")
    output_file.write("---------------------------\n")
    for x in range(len(candidates)):  
        output_file.write(f'{candidates[x]}: {pct[x]}% ({cand_votes[x]})\n') 
    output_file.write("---------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("---------------------------\n")
