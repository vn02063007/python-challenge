import os
import csv

csv_path = r'C:\Users\Tom B\Desktop\module\python-challenge\PyPoll\Resources\election_data.csv'

total_votes = 0
candidate_options = []
candidate_votes = {}

with open(csv_path) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)

    for row in reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

winning_candidate = ""
winning_count = 0
winning_percentage = 0
output = f"Election Results\n"
output += f"-------------------------\n"
output += f"Total Votes: {total_votes}\n"
output += f"-------------------------\n"
for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100
    output += f"{candidate_name}: {vote_percentage:.3f}% ({votes})\n"
    if (votes > winning_count) or (votes == winning_count and vote_percentage > winning_percentage):
        winning_count = votes
        winning_candidate = candidate_name
        winning_percentage = vote_percentage
output += f"-------------------------\n"
output += f"Winner: {winning_candidate}\n"
output += f"-------------------------\n"

print(output)

# Define the absolute path to the directory where you want to save the file
output_folder = os.path.abspath('C:\\Users\\Tom B\\Desktop\\module\\python-challenge\\PyPoll\\Analysis')

# Combine the output folder path with the desired file name to create the absolute path for the file
file_path = os.path.join(output_folder, 'analysis.txt')

# Open the file for writing and write the output to it
with open(file_path, 'w') as txt_file:
    txt_file.write(output)