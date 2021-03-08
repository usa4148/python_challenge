#
# Dan Cusick
# Data Scienct Boot Camp
# python-challenge PyBank
#
#
#
import os
import csv

pybank = os.path.join('.', 'PyBank.txt')
pybankwriter = open(pybank,'w')

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    monthly_pnl = 0
    pnl_total = 0
    pnl_max_value = 0
    pnl_min_value = 0
    pnl_max_date = "" 
    pnl_min_date = ""
    change_sum = 0
    previous_pnl = 0

    for row in csvreader:
        monthly_pnl = int(row[1])
        pnl_total = pnl_total + monthly_pnl
 
        if csvreader.line_num >=1:
            tmp_pnl = int(row[1])
            change_sum = change_sum + (tmp_pnl - previous_pnl)
            #print(f"tmp_pnl",tmp_pnl)
            if tmp_pnl > 0 and tmp_pnl > pnl_max_value:
                pnl_max_value = tmp_pnl
                pnl_max_date = row[0]
            if tmp_pnl <= 0 and tmp_pnl < pnl_min_value:
                pnl_min_value = tmp_pnl
                pnl_min_date = row[0]
            previous_pnl = tmp_pnl

    print("\n Financial Analysis \n","-----------------------------")
    print(" Total Months:", csvreader.line_num - 1)
    print(" Total: $", pnl_total)
    print(" Average Change: $", "{:.2f}".format(change_sum / (csvreader.line_num - 1)))
    print(" Greatest Increase in Profits: ", pnl_max_date, "($",pnl_max_value,")")
    print(" Greatest Decrease in Profits: ", pnl_min_date, "($",pnl_min_value,")")

    print("\n Financial Analysis \n","-----------------------------", file = pybankwriter)
    print(" Total Months:", csvreader.line_num - 1, file = pybankwriter)
    print(" Total: $", pnl_total, file = pybankwriter)
    print(" Average Change: $", "{:.2f}".format(change_sum / (csvreader.line_num - 1), file = pybankwriter))
    print(" Greatest Increase in Profits: ", pnl_max_date, "($",pnl_max_value,")", file = pybankwriter)
    print(" Greatest Decrease in Profits: ", pnl_min_date, "($",pnl_min_value,")", file = pybankwriter)