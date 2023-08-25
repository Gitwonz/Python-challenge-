#!/usr/bin/env python
# coding: utf-8

# In[54]:


import os
import csv

#read the csv file
csvpath = os.path.join(".", "Resources", "budget_data.csv")
fhandle = open(csvpath, 'r')
csvreader = csv.reader(fhandle, delimiter=",")

output_path = os.path.join(".", "financial_output.txt")

list_month = list()
list_prof = list()
list_change = list()
count = 0
sum = 0
kount = 0
summa = 0
greatest_increase = 0
best_month = ""
greatest_decrease = 0
worst_month = ""

#print csv header/title
print(csvreader)
header = next(csvreader)
print(f"csv header: {header}")

#To retrieve sum, counts, monthsand profit/losses

for line in csvreader:
    month = (line[0])
    nums = (line[1])
    intnums = int(line[1])
    count = count + 1
    sum = sum + intnums
    list_month.append(month)
    list_prof.append(nums)

#print(count)
#print(sum)
#print(list_month)
#print(list_prof)
#print(greatest_increase)
#print(best_month)
#print(greatest_decrease)
#print(worst_month)

#To calculate changes in Profit/Losses
#Use for loop to isolate changes to add to a list.
#To create a loop for retrieving th greatest_increase and greatest_decrease.
for i in range(len(list_prof)-1):
    change = int(list_prof[i+1]) - int(list_prof[i])
    list_change.append(change)
    
    if change > greatest_increase:
        greatest_increase = change
        best_month = list_month[i+1]
    elif change < greatest_decrease:
        greatest_decrease = change
        worst_month = list_month[i+1]

print(greatest_increase)
print(best_month)
print(greatest_decrease)
print(worst_month)
    

        
    


print(list_change)
#Implement sum and count of chance for average
for i in list_change:
    kount = kount+1
    summa = summa + int(i)

#print(kount)
#print(summa)
average_change = summa/kount
int_average_change = int(average_change)
print(average_change)

#max_list_change = max(list_change)
#min_list_change = min(list_change)
#print(max_list_change)
#print(min_list_change)

bank_output = open(output_path, 'w')

output = (f"Financial Analysis\n"
              f"---------------------------------\n"
              f"Total Months: {count}\n"
              f"Total: ${sum}\n"
         f"Average Change: ${int_average_change}\n"
         f"Greatest Increase in Profits: {best_month} (${greatest_increase})\n"
         f"Greatest Decrease in Profits: {worst_month} (${greatest_decrease})\n")

print(output)

bank_output.write(output)

