import csv
from datetime import datetime

with open('D:\Media/freshman_kgs.csv', 'r') as f:
    reader = csv.DictReader(f)
    results = []

    for column in reader:

        if column['Sex'] == 'M':

            sep_weight = float(column['Weight (Sep)'])
            apr_weight = float(column["Weight (Apr)"])

            weight_diff = apr_weight - sep_weight

            bmi_apr = float(column['BMI (Apr)'])
            if weight_diff >= 0 and bmi_apr > 20:
                column['Weight diff'] = weight_diff
                results.append(column)

    with open('D:\Media/freshman_kgs_new.csv', 'w', newline='') as f:
        fieldnames = reader.fieldnames + ['Weight diff']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for column in results:
            writer.writerow(column)
