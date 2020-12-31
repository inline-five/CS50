# import from libaries
from sys import argv
import csv


def main():
    if len(argv) != 3:  # should be (3) for actual program
        print("Usage: python dna.py data.csv sequence.txt")
        return 1

    # open database csv of people with STR pairs
    suspects = open(argv[1], "r")
    reader = csv.reader(suspects)
    people = []
    strs = []

    for row in reader:
        people.append(row)

    strs = people[0]  # assign first row of csv to strs
    strs.pop(0)  # delete name, off of the people csv import
    lenstrs = len(strs)  # lenght of STRs list

    for lists in people:
        sub_list_length = len(lists)

    for i in range(1, len(people)):  # turns STR repeats into ints
        for j in range(1, sub_list_length):
            people[i][j] = int(people[i][j])

    # open dna sequence as specified (1.txt) and load into memory
    f = open(argv[2], "r")
    seq = f.read()
    f.close()

    # come up with AGATC,AATG,TATC number of repeats in 1.txt
    strs_repeats_list = []
    for i in range(0, len(strs)):
        flag = True
        c_count = 0
        start = 0
        max_c_count = 0
        while flag:  # search for repeated STRs
            a = seq.find(strs[i], start)
            if a == -1:
                flag = False
            else:
                if (a - start + 1) == len(strs[i]):  # con seq
                    c_count += 1
                    if max_c_count <= c_count:
                        max_c_count = c_count
                if (a - start + 1) != len(strs[i]):  # new seq
                    c_count = 0
                start = a + 1
        strs_repeats_list.append(max_c_count + 1)  # add repeated STR counts to new list

    # compare people vs suspect STR lists
    match = False

    for item in people[1:]:
        if item[1:] == strs_repeats_list:
            match = True
            print(item[0])
        
    if match != True:
        print("No match")


if __name__ == "__main__":
    main()