import csv
csv.reader

input_file = '/workspaces/level-3-program-using-csv-multic4-cl/security_incidents.csv'
output_file = 'security_incidents_modified.csv'

with open(input_file, mode='r') as infile:
    reader = csv.reader(infile)
    data = list(reader)

new_column_name = 'status'
default_value = 'pending'

header = data[0] + [new_column_name]


rows = [row + [default_value] for row in data[1:]]

with open(output_file, mode='w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(header)
    writer.writerows(rows)

