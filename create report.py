import csv
with open("stat_report.csv", "r", encoding='utf-8') as csv_file:
    csv_content = csv.reader(csv_file)
    for row in csv_content:
        print(row)