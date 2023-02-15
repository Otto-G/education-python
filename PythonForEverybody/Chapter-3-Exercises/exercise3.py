limit = 5
for attempt in range(limit):
    while True:
        try:
            userEntered = input("Enter score (between 0 and 1): ")
            if type(userEntered) is str and userEntered.lower() == "q":
                quit = True
                break
            score = float(userEntered)
        except ValueError:
            print(f"Bad input {limit - attempt - 1} tries left")
            break

        if score > 1.0:
            print(f"Bad input {limit - attempt - 1} tries left")
            break
        elif score >= 0.9:
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

    if quit is True:
        break
