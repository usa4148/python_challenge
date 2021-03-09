#
# Dan C
# Data Scienct Boot Camp
# python-challenge PyBank
#
import os
import csv

pybank = os.path.join('.','analysis', 'PyBank.txt')
pybankwriter = open(pybank,'w')

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    monthly_pnl = 0
    pnl_total = 0
    pnl_max_value = 0
    pnl_min_value = 0
    pnl_max_key = "" 
    pnl_min_key = ""
    change_sum = 0
    previous_pnl = 0
    cnt = 0

    pnls = {}
    avg = {}


    for row in csvreader:
        cnt += 1
        pnls[row[0]] = int(row[1])
        
        pnl_total = pnl_total + int(row[1])
        if cnt > 1 :
            avg[row[0]] =int(row[1]) - previous_pnl
        change_sum = change_sum + int(row[1]) - previous_pnl
        previous_pnl = pnls.get(row[0])
        
    cnt = 0
    
    for key in avg:
        cnt +=1
        change_sum += avg[key]
    pnl_total = change_sum / cnt

    print(" cnt ",cnt ,"change_sum ", change_sum)  
    
    print("\n Financial Analysis \n","-----------------------------")
    print(" Total Months:", csvreader.line_num - 1)
    print(" Total: $", pnl_total)
    print(" Average Change: $", "{:.2f}".format(change_sum / (csvreader.line_num - 1)))
    grt_inc = max(avg, key=avg.get)
    print(" Greatest Increase",grt_inc,avg[grt_inc])
    grt_dec = min(avg, key=avg.get)
    print(" Greatest Decrease",grt_dec,avg[grt_dec])
    

    print("\n Financial Analysis \n","-----------------------------", file = pybankwriter)
    print(" Total Months:", csvreader.line_num - 1, file = pybankwriter)
    print(" Total: $", pnl_total, file = pybankwriter)
    print(" Average Change: $", "{:.2f}".format(change_sum / (csvreader.line_num - 1)), file = pybankwriter)
    print(" Greatest Increase",grt_inc,avg[grt_inc], file = pybankwriter)
    print(" Greatest Decrease",grt_dec,avg[grt_dec], file = pybankwriter)