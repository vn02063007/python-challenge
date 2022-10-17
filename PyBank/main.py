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


output = (
        f"Financial Analysis\n"
        f"----------------------------\n"
        f"Total Months: {Total_months}\n"
        f"Total: $ {total_net}\n"  

)
print (output)