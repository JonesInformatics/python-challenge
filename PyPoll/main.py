import csv, os

# setting variables to hold data

file_to_load = os.path.join( "Resources", "election_data.csv")
file_to_output = os.path.join( "analysis", "budget_analysis.txt")

# setting variables
total_votes = [] # integer
candidate_names = [] #string
num_votes_canidates = []
x = 0
store_vote_counts = []


#opening file
with open(file_to_load) as voting_data:
    reader=csv.reader(voting_data)
    next(reader)

    # iterating through csv 
    for row in reader: 
        
        total_votes.append(row[0])
        candidate_names.append(row[2])

    print (len(total_votes))

    
    for cand in (set(candidate_names)):
        x = 0
        voting_data.seek(1)
        reader=csv.reader(voting_data)
        for row in reader:
            if row[2] == cand:
                x += 1



        print(x)
        print(cand)