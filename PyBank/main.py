#
# Dan C
# Data Scienct Boot Camp
# python-challenge PyBank
#
import os
import csv

# Setup the path and open the Results file
pybank = os.path.join('.','analysis', 'PyBank.txt')
pybankwriter = open(pybank,'w')

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

# Open the CSV file, read a row and push past the header 
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # Create some vars and zero them
    pnl_total = 0
    change_sum = 0
    previous_pnl = 0
    cnt = 0

    # Create 2 dicts - one for the whole dataset, the other for the change deltas
    pnls = {}
    avg = {}

    # Process the cvs file, count th rows, sum total pnl
    for row in csvreader:
        cnt += 1
        pnls[row[0]] = int(row[1])
        pnl_total = pnl_total + int(row[1])

        # Load up the monthly change dict         if cnt > 1 :
            avg[row[0]] =int(row[1]) - previous_pnl
        change_sum = change_sum + int(row[1]) - previous_pnl
        previous_pnl = pnls.get(row[0])
        
    
    # Print to the console 
    print("\n Financial Analysis \n","-----------------------------")
    print(" Total Months:", csvreader.line_num - 1)
    print(" Total: ", '${0}'.format(pnl_total))
    print(" Average Change: ", "${:.2f}".format(change_sum / (csvreader.line_num - 1)))
    grt_inc = max(avg, key=avg.get)
    print(" Greatest Increase in Profits:",grt_inc,"(${0})".format(avg[grt_inc]))
    grt_dec = min(avg, key=avg.get)
    print(" Greatest Decrease in Profits:",grt_dec,"(${0})".format(avg[grt_dec]))
    
    # Print to the txt file
    print("\n Financial Analysis \n","-----------------------------", file = pybankwriter)
    print(" Total Months:", csvreader.line_num - 1, file = pybankwriter)
    print(" Total: ", '${0}'.format(pnl_total), file = pybankwriter)
    print(" Average Change: ", "${:.2f}".format(change_sum / (csvreader.line_num - 1)), file = pybankwriter)
    print(" Greatest Increase in Profits:",grt_inc,"(${0})".format(avg[grt_inc]), file = pybankwriter)
    print(" Greatest Decrease in Profits:",grt_dec,"(${0})".format(avg[grt_dec]), file = pybankwriter)