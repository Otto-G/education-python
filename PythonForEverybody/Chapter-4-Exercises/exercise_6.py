"Chapter 4: Exercise 6"
LIMIT = 5
LEAVE = False
for attempt in range(LIMIT):
    while True:
        try:
            user_entered = input("Enter score (between 0 and 1): ")
            if isinstance(user_entered, str) and user_entered.lower() == "q":
                LEAVE = True
                break
            score = float(user_entered)
        except ValueError:
            print(f"Bad input {LIMIT - attempt - 1} tries left")
            break

        if score > 1.0:
            print(f"Bad input {LIMIT - attempt - 1} tries left")
            break
        if score >= 0.9:
            GRADE = "A"
        elif score >= 0.8:
            GRADE = "B"
        elif score >= 0.7:
            GRADE = "C"
        elif score >= 0.6:
            GRADE = "D"
        else:
            GRADE = "F"

        print(GRADE)

    if LEAVE is True:
        break
