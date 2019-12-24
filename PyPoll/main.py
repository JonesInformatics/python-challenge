import csv, os

# setting variables to hold data

file_to_load = os.path.join( "Resources", "election_data.csv")
file_to_output = os.path.join( "analysis", "elections_results.txt")

# setting variables
total_votes = 0 # integer
candidate_names = [] # string
candidate_votes = {} # dictionary
x = 0
store_vote_counts = []
winning_count = 0


#opening file
with open(file_to_load) as voting_data:
    reader=csv.reader(voting_data)
    next(reader)

    # iterating through csv 
    for row in reader: 
        
        total_votes +=1
        name= row[2]


#finding unique candidate names
        if name not in candidate_names:
            candidate_names.append(row[2])
            candidate_votes[name]=0

        candidate_votes[name] +=1

# storing text to be printed out in text file
    output = (
        f"\nElection Results\n"
        f"================"
        f"\nTotal Votes: {total_votes}\n"
        f"================\n")

        
        
# converting candiate votes  to a percent
    for candidate in candidate_votes:
        votes=candidate_votes.get(candidate)
        vote_percentage = float(votes)/float(total_votes) * 100
# finding winner using if statement
        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate
# adding to output
        output += f"{candidate}: {vote_percentage:.3f}% ({votes})\n"

    output += (
        f"=============\n"
        f"Winner: {winning_candidate}\n"
        f"=============\n"
    )

# printing output to text file
    print(output)
    with open(file_to_output, 'w')as file_object:
        file_object.write(output)

       


    
    