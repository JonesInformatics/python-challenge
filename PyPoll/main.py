import csv, os

# setting variables to hold data

file_to_load = os.path.join( "Resources", "election_data.csv")
file_to_output = os.path.join( "analysis", "elections_results.txt")

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

    
    
    for cand in (set(candidate_names)):
        x = 0
        voting_data.seek(1)
        reader=csv.reader(voting_data)
        for row in reader:
            if row[2] == cand:
                x += 1



        # print(x)
        # print(cand)
        # print(x/(len(total_votes)))

    output = (
        f"Election Results\n"
        f"================"
        f"\nTotal Votes: {len(total_votes)}\n"
        f"================"
        f"\n{cand} ({x})\n"
        f"\n{cand} ({x})\n"
        f"\n{cand} ({x})\n"
        f"================"
        f"\nWinner:{cand} \n"
    )

    print(output)
    with open(file_to_output, 'w')as file_object:
        file_object.write(output)


    