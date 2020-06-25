import os           # import os library
import csv          # import csv library

# change the directory to the current working directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))
# set the path of the data csv file
input_file_path = os.path.join ( "Resources", "budget_data.csv")

net_profit = 0              # initialize the total profit/loss as zero
count_months = 0            # initialize no: of months as zero
profit_change = []          # create a list to store the change in profit/loss for each month
change_total = 0            # initialize the net profit/loss change as zero
first_row = True            # initialize the firstrow as true for the first month
prev_month_value = 0        # initialize the previous month profit/loass as zero for the first month

with open(input_file_path) as csvfile:          # open the datafile to be read
    file_reader = csv.reader(csvfile, delimiter=",")       # set the pointer to the file opened
    next(csvfile)                               # skip the header
    for eachrow in file_reader:                 # loop through all the records in the data file
        net_profit = net_profit + int(eachrow[1])       # add the current month profit/loss to the total
        count_months = count_months + 1                 # increment the number of months
        if first_row == True:                           # check if this is the first month
            prev_month_value = int(eachrow[1])          # current value will be the prev_month_value for the next month
            max_inc = int(eachrow[1])                   # initialize max increase as the current value
            max_dec = int(eachrow[1])                   # initialize max decrease as the current value
            first_row = False                           # set first row as False for the next records
        else:
            this_month_value = int(eachrow[1])          # read this month profit/loss from the current record
            this_month_change = this_month_value - prev_month_value     # calculate the change of profit/loss for this month
            change_total += this_month_change                           # add this month change to the total change in profit/loss  
            
            if(this_month_change > max_inc):                            # check if this month change is greater than max increase 
                max_inc = this_month_change                             # assign max increase as this month change if it is higher
                greatest_inc = {"month":eachrow[0], "value":max_inc}    # save this month name and the max increase value to a dictionary

            if(this_month_change < max_dec):                            # check if this month change is less than max decrease 
                max_dec = this_month_change                             # assign max decrease as this month change if it is less
                greatest_dec = {"month":eachrow[0], "value":max_dec}    # save this month name and the max decrease value to a dictionary

            prev_month_value = this_month_value                         # set the current value as prev_month_value for the next month

avg_change = round(change_total/(count_months-1),2)                     # calculate the average change and round it to 2 decimals

text_list = []                                                          # create a list to save the lines for displaying the results
text_list.append("\n````text")
text_list.append("Financial Analysis\n--------------------------")      # add a title for the results
text_list.append(f"Total Months:  {count_months}")                      # add the total number of months to the results list
text_list.append(f"Total:  ${net_profit}")                              # add the label and total profit/loss to the results
text_list.append(f"Average Change:  {'${:,.2f}'.format(avg_change)}")   # format the average change as currency
text_list.append(f"Greatest Increase in Profits:  {greatest_inc['month']}  ({'${:.0f}'.format(greatest_inc['value'])})")        # format and add the greatest increase in profit to the results
text_list.append(f"Greatest Decrease in Profits:  {greatest_dec['month']}  ({'${:.0f}'.format(greatest_dec['value'])}) ")       # format and add the greatest decrease to the results
text_list.append("`````\n")

for i in range(len(text_list)):         # print all the lines from the results list on the console
    print(text_list[i])

os.chdir(os.path.dirname(os.path.abspath(__file__)))    # go to the current path
output_path = os.path.join("Analysis", "analysis.txt")  # set path for text file to save the results

txt_writer = open(output_path, "w")         # open the text in write mode
for i in range(len(text_list)):             # loop through all the lines in results list
    txt_writer.write(text_list[i])          # write the line to the text file
    txt_writer.write("\n")                  # add a blank line to the text file



#--------------- Method 2  to print -------------------------
# print the results on to the console
# print("\n\n````text")
# print("Financial Analysis\n--------------------------")
# print(f"Total Months:  {count_months}")
# print(f"Total:  ${net_profit}")
# print(f"Average Change:  {'${:,.2f}'.format(avg_change)}")
# print(f"Greatest Increase in Profits:  {greatest_inc['month']}  ({'${:.0f}'.format(greatest_inc['value'])})")
# print(f"Greatest Decrease in Profits:  {greatest_dec['month']}  ({'${:.0f}'.format(greatest_dec['value'])}) ")
# print("`````\n")

# open a text file to save the results
# os.chdir(os.path.dirname(os.path.abspath(__file__)))
# output_path = os.path.join("Analysis", "analysis.txt")
# txt_writer = open(output_path, "w")

# write the results to the text file
# txt_writer.write("\n`````text")
# txt_writer.write("\nFinancial Analysis\n--------------------------")
# txt_writer.write(f"\nTotal Months:  {count_months}")
# txt_writer.write(f"\nTotal:  ${net_profit}")
# txt_writer.write(f"\nAverage Change:  {'${:,.2f}'.format(avg_change)}")
# txt_writer.write(f"\nGreatest Increase in Profits:  {greatest_inc['month']}  ({'${:.0f}'.format(greatest_inc['value'])})")
# txt_writer.write(f"\nGreatest Decrease in Profits:  {greatest_dec['month']}  ({'${:.0f}'.format(greatest_dec['value'])}) ")
# txt_writer.write("\n`````")