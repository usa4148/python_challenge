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
        
    #print(pnls)
    #print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    #print(avg)
    #print(cnt)
    #print("avg change", change_sum / cnt -1)
    
    
    #for k,v in avg.items():
    #    print("k",k," ","v",v)
    #    if v > pnl_max_value:
    #        pnl_max_key = k
    #        pnl_max_value = v
    #    if v < pnl_min_value:
    #        pnl_min_key = k
    #        pnl_min_value = v

    #tmp = max(avg, key=avg.get)
    #print("WTF::: ",avg[tmp])

    

    #pnl_max_key = max(avg, value=avg.get)
    #print("max key",pnl_max_key, pnl_max_value)
    ##pnl_min_key = min(avg, value=avg.get)
    #print("min key",pnl_min_key, pnl_min_value)

    #count = 0
    #csum = 0
    #for key in avg:
    #    count +=1
    #    csum += avg[key]
    #print("This is the mean: ", csum/count)
    


 
   #      if csvreader.line_num > 1:
        #For cvsreader.line_num:
    #        tmp_pnl = int(row[1])
    #        #print(cvsreader.line_num)
    #        change_sum = change_sum + (tmp_pnl - previous_pnl)
    #        print(change_sum," ", tmp_pnl)
    #        #print(f"tmp_pnl",tmp_pnl)
    #        if tmp_pnl > 0 and tmp_pnl > pnl_max_value:
    #            pnl_max_value = tmp_pnl
    #            pnl_max_date = row[0]
    #        if tmp_pnl <= 0 and tmp_pnl < pnl_min_value:
    #            pnl_min_value = tmp_pnl
    #            pnl_min_date = row[0]
    #    previous_pnl = tmp_pnl """

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