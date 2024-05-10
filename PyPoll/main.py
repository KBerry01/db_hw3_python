import csv
import os
csvpath = "Resources/election_data.csv"

os.chdir(os.path.dirname(os.path.realpath(__file__)))

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    total_votes = 0
    #create dictionary to hold canidate scores
    canidate_store = {}
    
    
    for row in csvreader:
        

        total_votes = total_votes + 1
    # Create list of canidates csv, then add rows each canidate name shows
        #Print(canidate,num_vote)

        canidate = row[2]
        
        if (canidate in canidate_store):
           
            canidate_store[canidate] = canidate_store[canidate] + 1
            
        else:

            canidate_store[canidate] = 1
        
        # For the total votes each candidate recieved / by total votes


output = f"""Election Results
-------------------------
Total Votes: {total_votes}
--------------------------\n"""
max_can = ""
max_votes = 0

for name in canidate_store.keys():
    perc_vote = (canidate_store[name] / total_votes) * 100  
    votes = canidate_store[name] 

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