"Chapter 5: Exercise 1"

USER_INPUT = None
TOTAL = 0
COUNT = 0
AVERAGE = 0
while USER_INPUT != "done":
    USER_INPUT = input("Enter a number: ")
    try:
        USER_INPUT = float(USER_INPUT)
        TOTAL += USER_INPUT
        COUNT += 1
        AVERAGE = TOTAL / COUNT
    except ValueError:
        if USER_INPUT == "done":
            continue

        print("Invalid input")

print(f"Total = {TOTAL} | Count = {COUNT} | Average = {AVERAGE}")
