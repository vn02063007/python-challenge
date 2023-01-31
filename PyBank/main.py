from distutils.text_file import TextFile
import os
import csv

csv_path = os.path.join("C:\\Users\\Tom B\\Desktop\\module\\python-challenge\\PyBank\\Resources\\budget_data.csv")

# List to store data
Total_months = 0
total_net = 0
net_change_list = []
month_of_change = []
Greatest_Increase = ["", 0]
Greatest_Decrease = ["", 9999999999999999999]

# read csv file
with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = next(csv_reader)

    first_row = next(csv_reader)
    Total_months += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])

    for row in csv_reader:
        Total_months += 1
        total_net += int(row[1])
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list.append(net_change)
        month_of_change.append(row[0])

        if net_change > Greatest_Increase[1]:
            Greatest_Increase[0] = row[0]
            Greatest_Increase[1] = net_change

        if net_change < Greatest_Decrease[1]:
            Greatest_Decrease[0] = row[0]
            Greatest_Decrease[1] = net_change

net_monthly_avg = sum(net_change_list) / len(net_change_list)

output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {Total_months}\n"
    f"Total: $ {total_net}\n"  
    f"Average Change: $ {net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {Greatest_Increase[0]} (${Greatest_Increase[1]})\n"
    f"Greatest Decrease in Profits: {Greatest_Decrease[0]} (${Greatest_Decrease[1]})\n"
)

# Print output
print (output)

# Export
# Define the absolute path to the directory where you want to save the file
output_folder = os.path.abspath('C:\\Users\\Tom B\\Desktop\\module\\python-challenge\\PyBank\\Analysis')

# Combine the output folder path with the desired file name to create the absolute path for the file
file_path = os.path.join(output_folder, 'analysis.txt')

# Open the file for writing and write the output to it
with open(file_path, 'w') as txt_file:
    txt_file.write(output)