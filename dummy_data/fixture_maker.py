import csv
import json
from datetime import datetime, time

json_array = []
writer = open('pop_fixture.json', 'w')

with open('pops.csv', newline='') as f:
    reader = csv.DictReader(f)
    csv_array= []
    pk = 1
    for row in reader:
        output = {
            "model" : "api.item",
            "pk" : pk,
            "fields" : {
                "number" : row['ITEM'],
                "description" : row['DESCRIPTION'],
                "p182_conversion" : row['Conversion Factor for P182']
            }
        }
        pk += 1
        json_array.append(output)


with open('employees.csv', newline='') as f:
    reader = csv.DictReader(f)
    csv_array= []
    pk = 1
    for row in reader:
        output = {
            "model" : "api.employee",
            "pk" : pk,
            "fields" : {
                "emp_id" : row['emp_id'],
                "first_name" : row['first_name'],
                "last_name"  : row['last_name'],
                "middle_name" : row['middle_name'],
                "suffix" : row["suffix"],
                "birth_date" : str(datetime.strptime(row["birth_date"], '%m/%d/%y').date(),),
                "language" : row["language"],
                "supervisor" : row["supervisor"],
                "manager" : row["manager"],
                "certificates" : row["certifications"],
                "med_restrictions" : row["med_restrictions"]
            }
        }
        pk += 1
        json_array.append(output)


# Just gonna construct shifts without csv.
shift_list = [1, 2, 3]
start_time = [time(7, 0, 0), time(15, 0, 0), time(23, 0, 0)]
end_time = [time(15, 0, 0), time(23, 0, 0), time(7, 0, 0)]

for i in range(len(shift_list)):
    output = {
        "model" : "api.shift",
        "pk" : i + 1,
        "fields" : {
            "number" : shift_list[i],
            "start_time" : start_time[i],
            "end_time" : end_time[i]

        }
    }
    json_array.append(output)

#Likewise for machines and lines.
line = ['A1', 'A2', 'B']

for i in range(len(line)):
    output = {
        "model" : "api.line",
        "pk" : i + 1,
        "fields" : {
            "number" : line[i]
        }
    }
    pk += 1
    json_array.append(output)


machines = [
    (1, 'A'), (1, 'B'), (1, 'C'),(1, 'D'),
    (1, 'E'), (1, 'F'), (2, 'G'), (2, 'H'),
    (2, 'J'), (2, 'K'), (2, 'R'), (2, 'S'),
    (3, 'L'), (3, 'M'), (3, 'N'), (3, 'P')
    ]

for i in range(len(machines)):
    output = {
        "model" : "api.machine",
        "pk" : i + 1,
        "fields" : {
            "name" : machines[i][1],
            "line" : machines[i][0]
        }
    }
    json_array.append(output)

#Save to json file.
json_data = json.dumps(json_array, indent=4, default=str)
writer.write(json_data)
