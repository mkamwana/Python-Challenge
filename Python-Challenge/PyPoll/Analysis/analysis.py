print ("hello world")
print ("hello world")

#specify the file path for elections file
poll_path=os.path.join("election_data.csv")

#open the csv file
with open (poll_path) as csv_file:
    poll_reader=csv.reader(csv_file, delimiter=",")
    
    #count no. of rows, less 1 (header row)
    rows= len(list(poll_reader))
    print("Total number of votes cast=", rows)
    
#create a dictionary from csv
with open (poll_path, encoding='utf-8-sig') as csvfile:
    poll_dic_reader=csv.reader(csvfile)
    
    
    #Define variables
votes = 0
winner_votes = 0
total_candidates = 0
greatest_votes = ["", 0]
candidate_options = []
candidate_votes = {}

     # Determine the the votes 
for row in poll_dic_reader:
    votes = votes + 1
    total_candidates = row[2] 
    if row[3] not in candidate_options:
        candidate_options.append(row[2])
        candidate_votes[row[2]] = 1
    else:
        candidate_votes[row[2]] = candidate_votes[row[2]] + 1

    # Getting the highest no. of votes
    if (votes > winner_votes):
        greatest_votes[1] = candidate_votes
        greatest_votes[0] = row[2]
