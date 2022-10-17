from distutils.text_file import TextFile
import os
import csv


csv_path = os.path.join('Resources','budget_data.csv')

#List to store data
Total_months = 0
Total = []
Change =[]
Greatest_Increse = []
Greatest_Decrease = []
total_net = 0
net_change_list = []
month_of_change = []

#def
def sum(data):
    date = str(data[0])
    profit = int(data[1])


#read csv file
with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = next(csv_reader)

    first_row = next(csv_reader)
    Total_months += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])

    for row in csv_reader:

# Total number of months
        Total_months += 1
#The net total amount of profit & losses
        total_net += int(row[1])
#Track the net change
        net_change = int(row[1])- prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]
        month_of_change += [row[0]]
#Calculate the greatest increase
if net_change > Greatest_Increse[1]:
        Greatest_Increse[0] = row[0]
        Greatest_Increse[1] = net_change
#Calculate the greatest decrease
if net_change < Greatest_Decrease[1]:
        Greatest_Decrease[0] = row[0]
        Greatest_Decrease[1] = net_change


#Average net change
net_monthly_avg= sum(net_change_list)/ len(net_change_list)

output = (
        f"Financial Analysis\n"
        f"----------------------------\n"
        f"Total Months: {Total_months}\n"
        f"Total: $ {total_net}\n"  
        f"Average Change: $ {net_monthly_avg:.2f}\n"
        f"Greatest Increase in Profits: {Greatest_Increse[0]} (${Greatest_Increse[1]})\n"
        f"Greatest Decrease in Profits: {Greatest_Decrease[0]} (${Greatest_Decrease[1]})\n"
)

#Print output
print (output)

#Export
with open('analysis',"w") as txt_file:
        TextFile.write('Analysis')