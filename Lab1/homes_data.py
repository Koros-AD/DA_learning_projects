import csv

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

            if rooms == 8:
                total_price += price
                count += 1

            if price > 180 and tax < 3500:
                column['Criteria'] = 'Yes'
            else:
                column['Criteria'] = 'No'

            new_columns.append(column)

        except ValueError:
            continue

    average_price = total_price / count
    print('Average price for homes with 8 rooms:', average_price)

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
