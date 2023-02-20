import os
import csv

#Define variables
total_months = 0 #summation
total_revenue = 0 #summation
revenue = [] #defines revenue as a column
previous_revenue = 0 #summation
month_of_change = [] #defines Month of change revenue as a column
revenue_change = 0 #summation
greatest_decrease = ["", 9999999] #Range
greatest_increase = ["", 0] #Range
revenue_change_list = []
revenue_average = 0 #summation
average_change= 0

#specify the file path for profits and losses
budget=os.path.join("./Resources/budget_data.csv")

#open the csv file
with open (budget, encoding='utf-8-sig') as csvfile:
    budget_dic_reader=csv.DictReader(csvfile)
    
    #count no. of rows, less 1 (header row)
    rows= len(list(budget_dic_reader))
    print("Total number of months analysed=", rows)
    
    #total revenue over the entire period
    total_revenue = total_revenue + int(row[1])
    print (total_revenue)
    
    #average change in revenue between months over the entire period
    previous_revenue = float(row[1])
    revenue_change = float(row[1])- previous_revenue
    print (revenue_change)
    
    revenue_change_list = revenue_change_list + [revenue_change]
    month_of_change = [month_of_change] + [row[0]]
    average_change==sum(revenue_change_list)%rows
    print (average_change)
    
    #The greatest increase in revenue (date and amount) over the entire period
    if revenue_change>greatest_increase[1]:
        greatest_increase[1]= revenue_change
        greatest_increase[0] = row[1]
#write changes to csv
results_file= os.path.join("./Resources/results_budget.txt")
with open(results_file, 'w') as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("---------------------\n")
    txt_file.write("Total Months: %d\n" % total_months)
    txt_file.write("Total Revenue: $%d\n" % total_revenue)
    txt_file.write("Average Revenue Change $%d\n" % revenue_average)
    txt_file.write("Greatest Increase in Revenue: %s ($%s)\n" % (greatest_increase[0], greatest_increase[1]))
    txt_file.write("Greatest Decrease in Revenue: %s ($%s)\n" % (greatest_decrease[0], greatest_decrease[1]))
