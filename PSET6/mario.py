from cs50 import get_int


while True: 
    height = get_int("Height: ")
    if height < 9 and height > 0:
        break

for i in range(height):
    
    for x in range(height - i - 1):
        print(" ", end="")
    
    for j in range(i + 1):
        print("#", end="")
    
    print("  ", end="")
    
    for j in range(i + 1):
        print("#", end="")
        
    print("")
