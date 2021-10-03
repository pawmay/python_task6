import sys

input_filename = sys.argv[1:][0]
output_filename = sys.argv[1:][1]
changes = sys.argv[1:][2:]
print(input_filename)
print(output_filename)
print(changes)

file = open(input_filename, 'r')
data = []
for line in file.readlines():
    splitted_line = line.split(';')
    data.append([splitted_line[0], splitted_line[1], splitted_line[2].replace('\n', '')])
file.close()

print(data)
