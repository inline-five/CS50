from cs50 import SQL  # allows use of SQL function
import csv
from sys import argv
# UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='students';


def main():

    if len(argv) != 2:
        print("Error with typing")
        return 1
        
    people = []
    names = []
    house = []
    birth = []
    
    db = SQL("sqlite:///students.db") 
    
    with open(argv[1], "r") as csvfile:
        reader = csv.reader(csvfile)
        
        people = list(reader)
        
    for i in people[1:]:
        names.append(i[0].split())
        house.append(i[1])
        birth.append(int(i[2]))
            
    for i in range(len(names)):
        if len(names[i]) == 2:
            db.execute("INSERT INTO students (first, last, house, birth) VALUES(?, ?, ?, ?)",
                       names[i][0], names[i][1], house[i], birth[i])
        if len(names[i]) == 3:
            db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",
                       names[i][0], names[i][1], names[i][2], house[i], birth[i])
                       

if __name__ == "__main__":
    main()