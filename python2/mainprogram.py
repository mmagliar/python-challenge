#analyzing the financial records of your company.
import os
import csv

month = 0
monthdollar2 = 0
previous = 0
current = 0
variance = 0
ytdvariance = 0
prev_line = None

#import csv file
csvpath = os.path.join('resource', 'election_data.csv')

with open(csvpath, newline='') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
      
    
# Read each row of data after the header
    for row in csvreader:
            #print(row)    
           
            month = month + 1
            monthdollar = (int(row[0]))
            monthdollar2 = monthdollar + monthdollar2 
                    
            previous = current
            current = monthdollar 
            variance = current - previous
            ytdvariance =  (variance + ytdvariance)
            percent = ((ytdvariance) / (month))