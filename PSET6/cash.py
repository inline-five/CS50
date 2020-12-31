from cs50 import get_float


def main():
    while True:
        change = get_float("Change owed: ")
        if change > 0:
            break

    cents = int(change * 100)

    print("Your change is:", cents)

    # check for quarters
    q = int(quarters(cents))
    print("Quarters:", q)
    
    # check for dimes
    d = int(dimes(cents, q))
    print("Dimes:", d)

    # check for nickels
    n = int(nickels(cents, q, d))
    print("Nickels:", n)

    # check for pennies
    p = int(pennies(cents, q, d, n))
    print("Pennies:", p)

    # add coins & print
    sum = q + d + n + p
    print(f"{sum}")


###############################
def quarters(cents):
    q = int(cents / 25)
    return q


def dimes(cents, q):
    d = int((cents - q*25) / 10)
    return d


def nickels(cents, q, d):
    n = int((cents - q*25 - d*10) / 5)
    return n


def pennies(cents, q, d, n):
    p = ((cents - q*25 - d*10 - n*5) / 1)
    return p
    
    
main()