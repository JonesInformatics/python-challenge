
import csv, os

file_to_load = os.path.join( "Resources", "budget_data.csv")
file_to_output = os.path.join( "analysis", "budget_analysis.txt")

# print(file_to_load)
# total_revenue = ([1])



#total_revenue = file_to_load[1]





total_revenue = 0
total_months = 0
pre_revenue = 0
month_of_change = []
revenue_change_list = []
greatest_increase = ["",0]
greatest_decrease = ["",999999999]

with open(file_to_load) as revenue_data:
    reader=csv.reader(revenue_data)

    for row in reader:
        total_months = total_months + 1
        # total_revenue = int(row["Profit/Losses"])

      # skip reading the header
      # 
      #   total_revenue += row[1]

        print(row[1])

    print(total_months)


#print total month outside of for loop


        




    
        

        
        

#         max_age = None
# oldest_person = None
# for row in input_file:
#     age = int(row["age"])
#     if max_age == None or max_age < age:
#         max_age = age
#         oldest_person = row["name"]

