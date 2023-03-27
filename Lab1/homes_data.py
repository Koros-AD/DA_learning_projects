# The program analyzes csv file and calculates the final average cost of a house with 8 rooms and creates new columns for houses with value over 180 and tax no less than 3500.
import csv
# reading file
with open('D:\Media/homes.csv', 'r') as file:
    reader = csv.DictReader(file)

    total_price = 0
    count = 0

    new_columns = []
    for column in reader:
        try:
            price = int(column['Sell'])
            tax = int(column['Taxes'])
            rooms = int(column['Rooms'])
# finding houses with 8 rooms
            if rooms == 8:
                total_price += price
                count += 1
# finding houses with value over 180 and tax no less than 3500
            if price > 180 and tax < 3500:
                column['Criteria'] = 'Yes'
            else:
                column['Criteria'] = 'No'

            new_columns.append(column)
# avoiding ValueError (computer starts with the wrong column)
        except ValueError:
            continue
#calculating average price
    average_price = total_price / count
    print('Average price for homes with 8 rooms:', average_price)
# writing a file with new data
    with open('D:\Media/homes_new.csv', 'w', newline='') as new_file:
        fieldnames = reader.fieldnames + ['Criteria', 'AvgPriceFor8Rooms']
        writer = csv.DictWriter(new_file, fieldnames=fieldnames)
        writer.writeheader()

        for row in new_columns:
            if row['Rooms'] == '8':
                row['AvgPriceFor8Rooms'] = average_price
            else:
                row['AvgPriceFor8Rooms'] = ''

            writer.writerow(row)
