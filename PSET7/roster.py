from cs50 import SQL  # allows use of SQL function
import csv
from sys import argv


def main():
    if len(argv) != 2:
        print("Error: Specify house name")
        return 1
    
    sql_return = []   
    
    db = SQL("sqlite:///students.db")
    house_select = argv[1]
    
    sql_return = db.execute("Select * FROM students WHERE house = ? ORDER BY last, first", house_select)
       
    for student in sql_return:
        print(student["first"], end=" ")
        if student["middle"] != None:
            print(student["middle"], end=" ")
        print(student["last"], end=", born ")
        print(student["birth"])
        
        
if __name__ == "__main__":
    main()