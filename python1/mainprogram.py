import os
import csv

totalmonths = []
totaldollars = []  
monthlychange = []
month = 0
monthdollar2 = 0
previous = 0
ytdvariance = 0
current = 0
variance = 0

#import csv file
csvpath = os.path.join('resource', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    
# Read each row of data after the header
    for row in csvreader:
        #print(row)    
        totalmonths.append(row[0])
        totaldollars.append(int(row[1]))

      
    for i in range(len(totaldollars)-1): 

        monthlychange.append(totaldollars[i+1]-totaldollars[i])   
        maxincrease = max(monthlychange)  
        maxloss =  min(monthlychange)
        maxgainmonth = monthlychange.index(max(monthlychange))+1    
        minlossmonth = monthlychange.index(min(monthlychange))+1   

        month = month + 1
        monthdollar = (int(row[1]))
        monthdollar2 = monthdollar + monthdollar2 
            
           # previous = current
            #current = monthdollar 
            #variance = current - previous
            #ytdvariance =  (variance + ytdvariance)
            #percent = ((ytdvariance) / (month))
            
          
print("Financial Analysis")
print("Total of months: " + str(month))
print(f"Total Dollars:  {'${:,.2f}'.format(sum(totaldollars))}")
print(f"Average Change:  {'${:,.2f}'.format(round(sum(monthlychange)/len(monthlychange),2))}")
print(f"Greatest Increase in Profits: {totalmonths[maxgainmonth]} {str('${:,.2f}'.format(maxincrease))}")
print(f"Greatest Decrease in Profits: {totalmonths[minlossmonth]} {str('${:,.2f}'.format(maxloss))}")


output_path = os.path.join('resource', 'output_data.csv')
with open(output_path, 'w', newline='') as csvfile:
   
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow([f"Total of months: " + str(month)])
    csvwriter.writerow([f"Total Dollars:  {'${:,.2f}'.format(sum(totaldollars))}\n"])
    csvwriter.writerow([f"Average Change:  {'${:,.2f}'.format(round(sum(monthlychange)/len(monthlychange),2))}\n"])
    csvwriter.writerow([f"Greatest Increase in Profits: {totalmonths[maxgainmonth]} {str('${:,.2f}'.format(maxincrease))}\n"])
    csvwriter.writerow([f"Greatest Decrease in Profits: {totalmonths[minlossmonth]} {str('${:,.2f}'.format(maxloss))}\n"])
    csvwriter.writerow(['---End of Analysis---'])