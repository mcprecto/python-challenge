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
    date_of_great_dec = 0
    great_inc_change = 0
    date_of_great_inc = 0

    for row in csvreader:
    
        curr_profit_loss = int(row[1])
        total_months = csvreader.line_num - 1
        if total_months > 1:
            change = curr_profit_loss - prev_profit_loss
            if change > great_inc_change:
                great_inc_change = change
                date_of_great_inc = row[0]
            elif change < great_dec_change:
                great_dec_change = change
                date_of_great_dec = row[0]
            total_change += change
            ave_change = total_change / (total_months -1)
            
        prev_profit_loss = curr_profit_loss

        total_profit_loss += curr_profit_loss

    
    print("Financial Analysis")
    print("--------------------------")

    print("Total Months: " + str(total_months))
    print("Total: $" + str(total_profit_loss))
    print("Average Change: $" + str(ave_change))
    print(date_of_great_dec)
    print(great_dec_change)
    print(date_of_great_inc)
    print(great_inc_change)

   