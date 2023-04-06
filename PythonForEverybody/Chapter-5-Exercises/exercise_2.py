"Chapter 5: Exercise 2"

USER_INPUT = None
TOTAL = 0
COUNT = 0
MAXIMUM = None
MINIMUM = None
while USER_INPUT != "done":
    USER_INPUT = input("Enter a number: ")
    try:
        USER_INPUT = float(USER_INPUT)
        TOTAL += USER_INPUT
        COUNT += 1
        if MAXIMUM is None or USER_INPUT > MAXIMUM:
            MAXIMUM = USER_INPUT
        if MINIMUM is None or USER_INPUT < MINIMUM:
            MINIMUM = USER_INPUT
    except ValueError:
        if USER_INPUT == "done":
            continue

        print("Invalid input")

print(f"Total = {TOTAL} | Maximum = {MAXIMUM} | Minumum = {MINIMUM}")
