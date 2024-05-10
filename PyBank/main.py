# Read in csv file
import os
import csv

csvpath = "Resources/budget_data.csv"

os.chdir(os.path.dirname(os.path.realpath(__file__)))

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

 # set my variables  
    profit_loss = 0 #code is good
    total_months = 0
    
# Create a list to hold changes
    last_month_profit = 0
    changes = []
    month_changes = []
# assign profit loss and date columns    
    for row in csvreader:
        column_value = int(row[1]) #code is good
        month = row[0]

# add up the total months included in csv       
# add up profit/loss for entire period    
        profit_loss += column_value
        total_months = total_months + 1
# Profit/loss change over entire period,
        if (total_months == 1):
            #grab last profit
            last_month_profit = int(row[1])
        else:
            change = int(row[1]) - last_month_profit
            changes.append(change)
            month_changes.append(row[0])

            # reset last_month_profit 
            last_month_profit = int(row[1])


# average of those changes (Divide by total count of changes)
# Calculate max and min for profit loss 
# Calculate greatest increase in profits (include date then amount)over entire period
# Calculate greatest decrease in profits (include date then amount)over entire period
avg_changes = sum(changes) / len(changes)
max_changes = max(changes)
max_month_indx = changes.index(max_changes)
max_month = month_changes[max_month_indx]
min_changes = min(changes)
min_month_indx = changes.index(min_changes)
min_month = month_changes[min_month_indx]
        


output = f"""Financial Analysis
 ----------------------------
Total Months: {total_months}
Total: ${profit_loss}
Average Change: {round(avg_changes, 2)}
Greatest Increase in Profits: ${max_changes, max_month}
Greatest Decrease in Profits: ${min_changes, min_month}"""
print(output)

with(open("output_Kenny.txt", 'w') as f):
    f.write(output)