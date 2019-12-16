# importing  
import csv, os

# loading data

file_to_load = os.path.join( "Resources", "budget_data.csv")
file_to_output = os.path.join( "analysis", "budget_analysis.txt")

# setting variables 

total_revenue = 0
total_months = 0
pre_revenue = 0
diff_revenue = 0
total_diff_revenue = 0
current_row_revenue = 0
ave_change_rev = 0
month_of_change = []
revenue_change_list = []
greatest_increase = ["",0]
greatest_decrease = ["",999999999]


# opening file
with open(file_to_load) as revenue_data:
    reader=csv.reader(revenue_data)
    next(reader)

# iterating through rows
    for row in reader:

       # finding total months
        total_months = total_months + 1
        
        # finding total revenue
        current_row_revenue = int(row[1])
        total_revenue += current_row_revenue  # DEBUG, int, strg error

        # setting if else statement to account for first row, i ncalculating average monthly change
        if pre_revenue == 0:
            diff_revenue = 0

        else:
            diff_revenue = current_row_revenue - pre_revenue

        total_diff_revenue += diff_revenue
        pre_revenue = current_row_revenue

ave_change_rev = total_diff_revenue/(total_months -1)


print(ave_change_rev)
print(pre_revenue)
print(total_months)
print(total_revenue)
 
print("Financial Analysis")
print("..................")
print(f"Total Months:   {total_months}")
print(f"Total Revenue:  {total_revenue}")
print(f"Average Monthly Change: {ave_change_rev}")




#print total month outside of for loop

# The average of the changes in "Profit/Losses" over the entire period

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in losses (date and amount) over the entire period


        




    
        

        
        


