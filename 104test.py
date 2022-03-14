import csv

with open("height-weight.csv", newline="") as f:
    reader= csv.reader(f)
    new_data= list(reader)

print(new_data[1][1])



