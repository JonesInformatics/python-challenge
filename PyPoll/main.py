import csv, os

# setting variables to hold data

file_to_load = os.path.join( "Resources", "election_data.csv")
file_to_output = os.path.join( "analysis", "budget_analysis.txt")

# setting variables
total_votes = [] # integer
candidate_names = [] #string
num_votes_canidates = [] # int


#opening file
with open(file_to_load) as voting_data:
    reader=csv.reader(voting_data)
    next(reader)

    # iterating through csv 
    for row in reader: 
        
        total_votes.append(row[0])
        candidate_names.append(row[2])



print("Election Results")
print(f"Total Number of Votes : {len(total_votes)}")
print(set(candidate_names))







