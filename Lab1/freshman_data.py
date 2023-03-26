#The program reads csv file and calculates the weight difference from September to April. According to the problem conditions, only male respondants 
# with BMI in April greater than 20 and non-negative weight difference are output.
import csv
from datetime import datetime
#reading the file
with open('D:\Media/freshman_kgs.csv', 'r') as f:
    reader = csv.DictReader(f)
    results = []
    
#calculating weight difference from Sep to Apr for male respondents
    for column in reader:

        if column['Sex'] == 'M':

            sep_weight = float(column['Weight (Sep)'])
            apr_weight = float(column["Weight (Apr)"])

            weight_diff = apr_weight - sep_weight
            
#setting condition for BMI and weight difference. If wd is >0 and BMI is 20> respondent is added to "results" list
            bmi_apr = float(column['BMI (Apr)'])
            if weight_diff >= 0 and bmi_apr > 20:
                column['Weight diff'] = weight_diff
                results.append(column)
                
#creating a file with new data, creating new column for Weight Difference
    with open('D:\Media/freshman_kgs_new.csv', 'w', newline='') as f:
        fieldnames = reader.fieldnames + ['Weight diff']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for column in results:
            writer.writerow(column)
