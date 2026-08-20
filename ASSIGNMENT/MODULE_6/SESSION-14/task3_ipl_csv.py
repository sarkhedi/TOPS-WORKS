import csv

with open("ipl_matches.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:
        
        print(row["Winner"])