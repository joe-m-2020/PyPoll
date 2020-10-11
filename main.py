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
    # use adder with nested for loop to find vote totals
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
    #find vote percentage
    total_votes = len(election_list)
    k_perc = kval / total_votes *100
    c_perc = cval / total_votes * 100
    l_perc = lval / total_votes * 100
    o_perc = oval / total_votes * 100
    winner = []
    
    winner.append(kval)
    winner.append(cval)
    winner.append(lval)
    winner.append(oval)
    election_winner = max(winner)
    
    #use dictionary to call the max value and link to name
    winner_dict = {kval:"Khan", cval : "Correy", lval : "Li", oval : "O'Tooley"}
    
    print("Election Results")
    l1 = ("Election Results\n")
    print("-------------------------")
    l2 = ("-------------------------\n")
    print(f"Total Votes:  {total_votes}")
    l3 = (f"Total Votes:  {total_votes}\n")
    print("-------------------------")
    l4 = "-------------------------\n"
    print(f"Khan: {round(k_perc)}.000%  ({kval})") 
    l5 = (f"Khan: {round(k_perc)}.000%  ({kval})\n")
    print(f"Correy: {round(c_perc)}.000%  ({cval})")
    l6 =(f"Correy: {round(c_perc)}.000%  ({cval})\n")
    print(f"Li: {round(l_perc)}.000%  ({lval})")
    l7 = (f"Li: {round(l_perc)}.000%  ({lval})\n")
    print(f"O'Tooley: {round(o_perc)}.000%  ({oval})")
    l8 = (f"O'Tooley: {round(o_perc)}.000%  ({oval})\n")
    print("-------------------------")
    l9 = "-------------------------\n"
    print(f"Winner: {winner_dict[election_winner]}")
    l10 = (f"Winner: {winner_dict[election_winner]}\n")
    print("-------------------------")
    l11 = "-------------------------\n"

    results_path = os.path.join("analysis", "results.txt")
    result_file = open(results_path,"w")
    result_file.write(l1)
    result_file.write(l2)
    result_file.write(l3)
    result_file.write(l4)
    result_file.write(l5)
    result_file.write(l6)
    result_file.write(l7)
    result_file.write(l8)
    result_file.write(l9)
    result_file.write(l10)
    result_file.write(l11)
    result_file.close