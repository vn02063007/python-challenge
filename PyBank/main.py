from email import header
from itertools import count
import os
import csv

csv_path = os.path.join('..','Resources','budget_data.csv')

#List to store data
Total_no_months = []
Net_total_profit_lost = []
Change =[]
Greatest_Increse = []
Greatest_Decrease = []

with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = next(csv_reader)

Total_no_months = count(csv_reader)

print(Total_no_months)