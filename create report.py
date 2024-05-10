import csv
csvFile = csv.reader("stat_report.csv")
for row in csvFile:
    print(row)