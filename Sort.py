import csv

from attr import field

data = []

with open('Brown Dwarfs.csv', 'r') as p:
    csvRead = csv.reader(p)
    for row in csvRead:
        data.append(row)

headers = data[0]
dwarf_data = data[1:]

temp = list(dwarf_data)
brown = []

brown.append(headers)

for dwarfData in temp:
    dwarf_mass = dwarfData[4]
    if dwarf_mass == '':
        dwarf_data.remove(dwarfData)
        continue
    else:
        dwarf_mass_value = float(dwarf_mass)* 0.000954588   
        dwarfData[4] = dwarf_mass_value

    dwarf_radius = dwarfData[5]
    if dwarf_radius == '':
        dwarf_data.remove(dwarfData)
        continue
    else:
        dwarf_radius_value = float(dwarf_radius)* 0.000954588   
        dwarfData[5] = dwarf_radius_value

        brown.append(dwarfData)

star = []
with open('StarResearch.csv', 'r') as f:
    csvRead = csv.reader(f)
    for row in csvRead:
        star.append(row)

headers_1 = brown[0]
brown_data = brown[1:]

headers_2 = star[0]
star_data = star[1:]

headers = headers_1 + headers_2
entire_data = []

for index, data_row in enumerate(star_data):
    entire_data.append(star_data[index] + brown_data[index])

with open('Merged_data.csv', 'w') as f:
    csvWrite = csv.writer(f)
    csvWrite.writerow(headers)
    csvWrite.writerows(entire_data)

with open('Merged_data.csv') as input, open('Merged_data1.csv', 'w', newline = '') as output:
    writer = csv.writer(output)
    for row in input:
        if any(field.strip() for field in row):
            writer.writerow(row)