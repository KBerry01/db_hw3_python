import csv
import os
csvpath = "Resources/election_data.csv"

os.chdir(os.path.dirname(os.path.realpath(__file__)))

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    total_votes = 0
    #create dictionary to hold canidate scores
    candidate_store = {}
    
    
    for row in csvreader:
        

        total_votes = total_votes + 1
    # Create list of canidates csv, then add rows each canidate name shows
        #Print(canidate,num_vote)

        candidate = row[2]
        
        if (candidate in candidate_store):
           
            candidate_store[candidate] = candidate_store[candidate] + 1
            
        else:

            candidate_store[candidate] = 1
        
        


output = f"""Election Results
-------------------------
Total Votes: {total_votes}
--------------------------\n"""
max_can = ""
max_votes = 0

for name in candidate_store.keys():
    # For the total votes each candidate recieved / by total votes
    perc_vote = (candidate_store[name] / total_votes) * 100  
    votes = candidate_store[name] 

    line = f"{name}: {round(perc_vote, 3)}% ({votes})\n"
    output += line

    if votes > max_votes:
       max_can = name
       max_votes = votes

last_line = f"""-----------------
Winner: {max_can}"""

output += last_line

print(output)

with(open("output_Kenny.txt #2", 'w') as f):
    f.write(output)