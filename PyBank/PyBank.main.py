import os
import csv

csvpath = os.path.join(os.path.dirname(os.path.abspath(__file__)),"../..", "Instructions", "PyBank","Resources", "budget_data.csv")

with open(csvpath, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    # print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
        
    total_profit_loss = 0
    total_months = 0
    total_change = 0
    ave_change = 0
    great_dec_change = 0
    great_inc_change = 0

    for row in csvreader:
    
        curr_profit_loss = int(row[1])
        total_months = csvreader.line_num - 1
        if total_months > 1:
            change = curr_profit_loss - prev_profit_loss
            if change > great_inc_change:
                great_inc_change = change
            elif change < great_dec_change:
                great_dec_change = change
            total_change += change
            ave_change = total_change / (total_months -1)
            
        prev_profit_loss = curr_profit_loss

        total_profit_loss += curr_profit_loss

    
    print("The total number of months included in the data set is " + str(total_months) + ".")
    print(str(total_profit_loss))
    print(str(ave_change))
    print(great_dec_change)
    print(great_inc_change)

   