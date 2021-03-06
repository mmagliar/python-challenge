#analyzing the election date
import os
import csv
#import csv file
csvpath = os.path.join('resource', 'election_data.csv')

electionresults = { }
totalvotes = 0  

with open(csvpath, newline='') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
   
# Read each row of data after the header
    for row in csvreader:
        totalvotes += 1    
        if row[2] not in electionresults:
            electionresults[row[2]]=1
        else:
            electionresults[row[2]]+=1  

candidatevotes = list(electionresults.keys())     
results = list(electionresults.values())

#Testing set
#print(candidatevotes)
#print(electionresults)
#print(results)

print("Election Results")
print("------------------------------")
print(f"Total Votes: {'{:,.0f}'.format(totalvotes)}")
print("------------------------------")
#print(f"{candidatevotes[0]}: {'{:,.0f}'.format(results[0])}")
#print((candidatevotes[0]), (results[0]))
#print((candidatevotes[0]), (candidatevotes[1]), (results[0]))
print(f"{candidatevotes[0]}: {'{:,.0f}'.format(results[0]/totalvotes*100)}% ({'{:,.0f}'.format(results[0])})")
print(f"{candidatevotes[1]}: {'{:,.0f}'.format(results[1]/totalvotes*100)}% ({'{:,.0f}'.format(results[1])})")
print(f"{candidatevotes[2]}: {'{:,.0f}'.format(results[2]/totalvotes*100)}% ({'{:,.0f}'.format(results[2])})")
print(f"{candidatevotes[3]}: {'{:,.0f}'.format(results[3]/totalvotes*100)}% ({'{:,.0f}'.format(results[3])})")
print(f"Winner: ",  (candidatevotes[0]))
 
 
#=============================================================
output_path = os.path.join('resource', 'output_data.csv')
with open(output_path, 'w', newline='') as csvfile:
   
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['----------------------'])
    csvwriter.writerow([f"Total Votes: {'{:,.0f}'.format(totalvotes)}"])
    csvwriter.writerow(['----------------------'])
    csvwriter.writerow([f"{candidatevotes[0]}: {'{:,.0f}'.format(results[0]/totalvotes*100)}% ({'{:,.0f}'.format(results[0])}\n"])
    csvwriter.writerow([f"{candidatevotes[1]}: {'{:,.0f}'.format(results[1]/totalvotes*100)}% ({'{:,.0f}'.format(results[1])}\n"])
    csvwriter.writerow([f"{candidatevotes[2]}: {'{:,.0f}'.format(results[2]/totalvotes*100)}% ({'{:,.0f}'.format(results[2])}\n"])
    csvwriter.writerow([f"{candidatevotes[3]}: {'{:,.0f}'.format(results[3]/totalvotes*100)}% ({'{:,.0f}'.format(results[3])}\n"])
    csvwriter.writerow(["Winner: ",  (candidatevotes[0])])
    csvwriter.writerow(['---End of Analysis---'])