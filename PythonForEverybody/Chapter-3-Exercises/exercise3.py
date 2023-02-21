limit = 5
leave = False
for attempt in range(limit):
    while True:
        try:
            user_entered = input("Enter score (between 0 and 1): ")
            if isinstance(user_entered, str) and user_entered.lower() == "q":
                leave = True
                break
            score = float(user_entered)
        except ValueError:
            print(f"Bad input {limit - attempt - 1} tries left")
            break

        if score > 1.0:
            print(f"Bad input {limit - attempt - 1} tries left")
            break
        if score >= 0.9:
            grade = "A"
        elif score >= 0.8:
            grade = "B"
        elif score >= 0.7:
            grade = "C"
        elif score >= 0.6:
            grade = "D"
        else:
            grade = "F"

        print(grade)

    if leave is True:
        break
