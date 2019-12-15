import csv, os

file_to_load = os.path.join( "Resources", "budget_data.csv")
file_to_output = os.path.join( "analysis", "budget_analysis.txt")


# # total_revenue = ([1])


total_revenue = 0
total_months = 0
pre_revenue = 0
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
        total_months = total_months + 1
        # # # total_revenue = int(row["Profit/Losses"])

      
        # # # # # total_revenue += (row[1]) DEBUG, int, strg error
    
    
# # # print(row[1])
        #print(row[1])
    print("Financial Analysis")
    print("..................")
    print(f"Total Months:   {total_months}")


#print total month outside of for loop

# The average of the changes in "Profit/Losses" over the entire period

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in losses (date and amount) over the entire period


        




    
        

        
        


