import os
import csv

os.chdir(os.path.dirname(os.path.abspath(__file__)))
input_file_path = os.path.join ( "Resources", "election_data.csv")

candidates_dict = {}
count_votes = 0
with open(input_file_path) as csvfile:
    file_reader = csv.reader(csvfile, delimiter=",")
    next(csvfile)
    for eachrow in file_reader:
        count_votes = count_votes + 1
        if eachrow[2] not in candidates_dict:
            candidates_dict[eachrow[2]] = 1
        elif eachrow[2] in candidates_dict:
            candidates_dict[eachrow[2]] += 1       

winner_name = max(candidates_dict, key=candidates_dict.get)     

results = []
results.append("\n````text")
results.append("Election Results\n-------------------------------")
results.append(f"Total Votes:  {count_votes}")
results.append("-------------------------------")
for (x,y) in candidates_dict.items():
    vote_perc = float(float(y)/float(count_votes))
    vote_perc = '{:,.3%}'.format(vote_perc)
    results.append(f"{x}:  {vote_perc}   ({y})")
results.append("-------------------------------")
results.append(f"Winner:  {winner_name}")
results.append("-------------------------------")
results.append("`````\n")

for i in range(len(results)):
    print(results[i])

os.chdir(os.path.dirname(os.path.abspath(__file__)))    # go to the current path
output_path = os.path.join("Analysis", "analysis.txt")  # set path for the output file

txt_writer = open(output_path, "w")
for i in range(len(results)):
    txt_writer.write(results[i])
    txt_writer.write("\n")
