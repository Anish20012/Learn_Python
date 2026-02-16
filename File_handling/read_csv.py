'''import csv

with open('data.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if not row: # Skips empty rows
            continue
        # Process the row here
        # Example:
        # print(row[0], row[1])'''


import csv

with open("data.csv", "r") as file:
    lines = file.readlines()

    for line in lines[1:]:   #skip header
        coloumn = line.strip().split(',')
        print(coloumn[1])  #name column'''