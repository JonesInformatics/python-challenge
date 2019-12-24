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
        total_revenue += current_row_revenue  

        # setting if else statement to account for first row, in calculating average monthly change
        if pre_revenue == 0:
            diff_revenue = 0

        else:
            diff_revenue = current_row_revenue - pre_revenue

        total_diff_revenue += diff_revenue
        pre_revenue = current_row_revenue

        if diff_revenue > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1]= diff_revenue
            
        if diff_revenue < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1]= diff_revenue

ave_change_rev = total_diff_revenue/(total_months -1)

output = (
f"\nFinancial Analysis\n"
f"=================\n"
f"Total Months:   {total_months}\n"
f"Total Revenue:  {total_revenue}\n"
f"Average Monthly Change: {ave_change_rev}\n"
f"Greatest Increase in revenue: {greatest_increase[0]} ${greatest_increase[1]}\n"
f"Greatest Decrease in revenue: {greatest_decrease[0]} ${greatest_decrease[1]}\n"
)
print(output)
with open(file_to_output, 'w')as file_object:
    file_object.write(output)





        




    
        

        
        


