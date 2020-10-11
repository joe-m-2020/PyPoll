import os

#module for reading csv files
import csv

# from csv import reader
election_csv = os.path.join('resources', 'election_data.csv')

with open(election_csv,'r') as python_csvfile:
    election_data = csv.reader(python_csvfile, delimiter=',')
    header = next(election_data)
    
    election_list = []
    for line in election_data:
        election_list.append(list(line))

    klist = []
    kval = 0
    cval = 0
    lval = 0
    oval = 0
    for rows in election_list:
        for i in rows:
            if(i=="Khan"):
                kval = kval+1
            elif(i=="Correy"):
                cval = cval+1
            elif(i=="Li"):
                lval = lval +1
            elif(i=="O'Tooley"):
                oval = oval +1 
                
    print("Election Results")
    l1 = ("Election Results\n")
    print("-------------------------")
    l2 = ("-------------------------\n")
    total_votes = len(election_list)
    print(f"Total Votes:  {total_votes})")
    l3 = (f"Total Votes:  {total_votes}\n")
