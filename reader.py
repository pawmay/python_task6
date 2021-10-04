import sys
import os

def validate_numbers(number):
    try:
        return int(number)
    except ValueError:
        print("Error: enter the row / column number!")
        sys.exit()
    except NameError:
        print("Error: variable error!")
        sys.exit()

input_filename = sys.argv[1:][0]
output_filename = sys.argv[1:][1]
changes = sys.argv[1:][2:]

try:
    file = open(input_filename, 'r')
except FileNotFoundError:
    print("Error: no file!")
    for f in os.listdir('.'):
        if os.path.isfile(f):
            print(f)
    sys.exit()

data = []
for line in file.readlines():
    splitted_line = line.split(';')
    data.append([splitted_line[0], splitted_line[1], splitted_line[2].replace('\n', '')])
file.close()


for change in changes:
    i = validate_numbers(change.split(',')[0])
    j = validate_numbers(change.split(',')[1])
    new_value = (change.split(',')[2])
    if i and j:
        data[i][j] = new_value

with open(output_filename, 'w') as file2:
    rows = ''
    for row in data:
        rows = rows + row[0] + ';' + row[1] + ';' + row[2] + '\n'
    file2.write(rows)
