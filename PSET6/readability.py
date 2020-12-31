from cs50 import get_string


def main():

    letters = 0
    words = 1
    sentences = 0
    other = 0

    # ask user for text
    sentence = get_string("Text: ")

    # count number of letters
    # a to z
    for i in sentence:
        if i.isalpha():
            letters += 1
        elif i.isspace():
            words += 1
        elif i == "?" or i == "." or i == "!":
            sentences += 1

    l = 100 / words * letters
    s = 100 / words * sentences

    level = round(0.0588 * l - 0.296 * s - 15.8)

    if level < 1:
        print("Before Grade 1")
    if level >= 1 and level < 16:
        print(f"Grade {level}")
    if level >= 16:
        print("Grade 16+")


main()