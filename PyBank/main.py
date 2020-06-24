import os
import csv

# os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
input_file_path = os.path.join ( "Resources", "budget_data.csv")

net_profit = 0
count_months = 0
profit_change = []
change_total = 0
first_row = True
prev_month_value = 0
with open(input_file_path) as csvfile:
    file_reader = csv.reader(csvfile, delimiter=",")
    next(csvfile)
    for eachrow in file_reader:
        # print(eachrow)
        net_profit = net_profit + int(eachrow[1])
        count_months = count_months + 1
        if first_row == True:
            prev_month_value = int(eachrow[1])
            max_inc = int(eachrow[1])
            max_dec = int(eachrow[1])
            first_row = False
        else:
            this_month_value = int(eachrow[1])
            this_month_change = this_month_value - prev_month_value
            change_total += this_month_change
            
            if(max_inc < this_month_change):
                max_inc = this_month_change
                greatest_inc = {"month":eachrow[0], "value":max_inc}

            if(max_dec > this_month_change):
                max_dec = this_month_change
                greatest_dec = {"month":eachrow[0], "value":max_dec}

            prev_month_value = this_month_value

avg_change = round(change_total/(count_months-1),2)

print("\n\n````text")
print("Financial Analysis\n--------------------------")
print(f"Total Months:  {count_months}")
print(f"Total:  ${net_profit}")
print(f"Average Change:  {'${:,.2f}'.format(avg_change)}")
print(f"Greatest Increase in Profits:  {greatest_inc['month']}  ({'${:.0f}'.format(greatest_inc['value'])})")
print(f"Greatest Decrease in Profits:  {greatest_dec['month']}  ({'${:.0f}'.format(greatest_dec['value'])}) ")
print("`````\n")

os.chdir(os.path.dirname(os.path.abspath(__file__)))
output_path = os.path.join("Analysis", "analysis.txt")

txt_writer = open(output_path, "w")
txt_writer.write("\n`````text")
txt_writer.write("\nFinancial Analysis\n--------------------------")
txt_writer.write(f"\nTotal Months:  {count_months}")
txt_writer.write(f"\nTotal:  ${net_profit}")
txt_writer.write(f"\nAverage Change:  {'${:,.2f}'.format(avg_change)}")
txt_writer.write(f"\nGreatest Increase in Profits:  {greatest_inc['month']}  ({'${:.0f}'.format(greatest_inc['value'])})")
txt_writer.write(f"\nGreatest Decrease in Profits:  {greatest_dec['month']}  ({'${:.0f}'.format(greatest_dec['value'])}) ")
txt_writer.write("\n`````")