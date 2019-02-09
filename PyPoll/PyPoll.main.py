import os
import csv

csvpath = os.path.join(os.path.dirname(os.path.abspath(__file__)),"../..","Instructions", "PyPoll", "Resources", "election_data.csv")

with open(csvpath, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # initialize all variables
    total_votes = 0
    candidates_list = []
    count_per_candidate = []
    percent_per_candidate = 0
    most_count_candidate = 0

    for row in csvreader:
        # compute total number of votes cast
        total_votes = csvreader.line_num - 1

        if total_votes > 1:
            #store names of unique candidates in list (remember without this, lists went back to being empty and did not store new candidate name after append for each iteration)
            new_candidates_list = candidates_list
            new_count_per_candidate = count_per_candidate

            if row[2] in new_candidates_list:
                # finds the index number of the candidate in current row
                candidate_index = int(new_candidates_list.index(row[2]))
                # adds one vote to counter of appropriate candidate
                new_count_per_candidate[candidate_index] += 1
                # calculates percentages of total vote per candidate
                percent_per_candidate = [round((count/(total_votes-1))*100,2) for count in new_count_per_candidate]
                # finds the highest number of votes in new_count_per_candidate
                winner = max(new_count_per_candidate)
                # finds the index of the max number in new_count_per_candidate and uses same to access winner name
                winner_name = new_candidates_list[int(new_count_per_candidate.index(winner))]
            else:
                # each new candidate is stored in candidates_list with a corresponding vote counter in vote_per_candidate
                candidates_list.append(row[2])
                count_per_candidate.append(1)
                

print("-------------------------------")
print("Election Results")
print("-------------------------------")

print ("Total Votes: " + str(total_votes))
print("-------------------------------")

for i in range(4):
    print(new_candidates_list[i] + ": " + str(percent_per_candidate[i]) + "%   " + str(new_count_per_candidate[i]))

print("-------------------------------")
print("Winner: " + winner_name)
print("-------------------------------")