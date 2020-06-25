import os           # import os library
import csv          # import csv library

# change the directory to the current working directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))
# set the path of the data csv file
input_file_path = os.path.join ( "Resources", "election_data.csv")

candidates_dict = {}        # create a dictionary to save the candidate name and the votes they earned
count_votes = 0             # initialize total votes to zero
with open(input_file_path) as csvfile:                  # open the datafile to be read
    file_reader = csv.reader(csvfile, delimiter=",")    # set the pointer to the file opened
    next(csvfile)                                       # skip the header
    for eachrow in file_reader:                 # loop through all the rows in the data file
        count_votes = count_votes + 1           # increment the total number of votes as it loops through each row
        if eachrow[2] not in candidates_dict:   # check if this candidate is in the dictionary
            candidates_dict[eachrow[2]] = 1     # add the candidate name to the dictionary if it is not there
        elif eachrow[2] in candidates_dict:
            candidates_dict[eachrow[2]] += 1    # add one vote to the candidate if the name is already there in the dictionary

winner_name = max(candidates_dict, key=candidates_dict.get)     # fetch the key/candidate name from the dictionary where the value/votes is maximum

results = []                                        # create a list to store all the lines required to display the result
results.append("\n````text")
results.append("Election Results\n-------------------------------") # add a title for the results to be displayed
results.append(f"Total Votes:  {count_votes}")      # add total number of votes to the results list
results.append("-------------------------------")   # add a line to the results list
for (x,y) in candidates_dict.items():               # loop through the items in the dictionary
    vote_perc = float(y / count_votes)              # calculate the votes precentage for the current candidate
    vote_perc = '{:,.3%}'.format(vote_perc)         # format the value as precentage and rounded to 3 decimals
    results.append(f"{x}:  {vote_perc}   ({y})")    # add the line to the results list
results.append("-------------------------------")   # add a line to the results list
results.append(f"Winner:  {winner_name}")           # add winner name to the results
results.append("-------------------------------")   # add a line to the results list
results.append("`````\n")                           

for i in range(len(results)):       # loop through the results list
    print(results[i])               # display each line on the console

os.chdir(os.path.dirname(os.path.abspath(__file__)))    # go to the current path
output_path = os.path.join("Analysis", "analysis.txt")  # set path for the output file

txt_writer = open(output_path, "w")     # open the text file to write
for i in range(len(results)):           # loop through the results list
    txt_writer.write(results[i])        # print the result list into the text file
    txt_writer.write("\n")              # print a blank line
