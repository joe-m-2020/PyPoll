import os

#module for reading csv files
import csv
from csv import reader
election_csv = os.path.join('resources', 'election_data.csv')

with open(election_csv,'r') as read_obj:
    csv_reader = reader(read_obj)
    list_of_rows = list(csv_reader)

candidates = {"Khan": 0, "Correy": 0, "Li": 0, "O'tooley": 0}

    
# read file

# Results
print("Election Results")
l1 = "Election Results\n"
print("-------------------------")
l2 = "-------------------------\n"
total_votes = len(list_of_rows)-1
print(f"Total Votes:  {total_votes)")
l3 = f"Total Votes:  {total_votes)}\n"