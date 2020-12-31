from sys import argv
import csv
import math
import pprint

## Conversion from hours:mins to hours:tenths
def convert_mins(time):
    hours = math.floor(time/60)
    mins = round(time - hours * 60)
    mins_dict = {
        range(0,4): .0,
        range(4,10): .1,
        range(10,16): .2,
        range(16,22): .3,
        range(22,28): .4,
        range(28,34): .5,
        range(34,40): .6,
        range(40,46): .7,
        range(46,52): .8,
        range(52,58): .9,
        range(58,60): 1.0
    }
    calc_mins = list(({mins_dict[key] for key in mins_dict if mins in key}))
    return hours + calc_mins[0]

## change a/c type to type rating type
def swap_type(airplane):
    airplane_dict = {
        'A319': 'A-320',
        'A320': 'A-320',
        'A321': 'A-320',
        'B737': 'B-737',
        'B757': 'B-757',
        'B767': 'B-767',
        'B777': 'B-777',
        'B787': 'B-787',
        'MD80': 'DC-9'
    }
    return airplane_dict[airplane]

## global variables
logbook_list = []
row_count = 0
duplicate_row = 0
aircraft_types = ['A319', 'A320', 'A321', 'B737', 'B757', 'B767', 'B777', 'B787', 'MD80']

## read csv file into memory into logbook_list []
with open('logbook_extract.csv', 'r') as csvfile:
    logbook = csv.reader(csvfile, delimiter=',')
    for row in logbook:
        logbook_list.append(row)
        row_count += 1

for i in range(row_count-1):
    if logbook_list[i][40] == logbook_list[i+1][40]:
        duplicate_row += 1

row_count -= duplicate_row

## delete duplicate rows
for i in range(row_count-1):
    if logbook_list[i][40] == logbook_list[i+1][40]:
        logbook_list.pop(i+1)

## create header and pop off first row to delete header row
header = logbook_list[0]
header_len = len(header)
logbook_list.pop(0)
row_count -= 1


## convert flt time and a/c types
for row in logbook_list:
    if row[47] != '1':
        if row[61] != 'NULL' and row[61] in aircraft_types:
            row[61] = swap_type(row[61])
        if row[46] != 'NULL' and row[46] != '0':
            row[46] = convert_mins(int(row[46]))

i = 0
## Combine hours on a per day basis
for i in range(85):
    if (logbook_list[i][38] == logbook_list[i+1][38] and logbook_list[i+1][47] != '1'):
        logbook_list[i][int(46)] += logbook_list[i+1][int(46)]
        logbook_list[i][37] = logbook_list[i][37] + '-' + logbook_list[i+1][37]
        logbook_list.pop(i+1)
        row_count -= 1
    elif (logbook_list[i][38] == logbook_list[i-1][38] and logbook_list[i][47] != '1'):
        logbook_list[i-1][int(46)] += logbook_list[i][int(46)]
        logbook_list[i-1][37] = logbook_list[i-1][37] + '-' + logbook_list[i][37]
        logbook_list.pop(i)
        row_count -= 1



## write new file using data in logbook_list[]
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['DATE', 'MODEL', 'IDENT', 'RTE', 'DURATION', 'NIGHT', 'XTY', 'SIC', 'PIC', 'REMARKS'])

    for i in range(row_count-1):
        ## FO input    chk valid valid #               check DH           check valid flt time                                                check position
        if logbook_list[i][61] != 'NULL' and logbook_list[i][47] != '1' and logbook_list[i][46] != 'NULL' and logbook_list[i][46] != '0' and logbook_list[i][0] != "CA":
            writer.writerow([logbook_list[i][38], logbook_list[i][61], logbook_list[i][59], logbook_list[i][36] + '-' + logbook_list[i][37], round(logbook_list[i][46], 2), '', round(logbook_list[i][46], 2), round(logbook_list[i][46], 2), '', ''])
        ## CA input    chk DH                          check DH           check valid flt time                                                check position
        if logbook_list[i][61] != 'NULL' and logbook_list[i][47] != '1' and logbook_list[i][46] != 'NULL' and logbook_list[i][46] != '0' and logbook_list[i][0] == "FO":
            writer.writerow([logbook_list[i][38], logbook_list[i][61], logbook_list[i][59], logbook_list[i][36] + '-' + logbook_list[i][37], logbook_list[i][46], '', round(logbook_list[i][46], 2), round(logbook_list[i][46], 2), '', ''])