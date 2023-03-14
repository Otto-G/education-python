"Chapter 4: Exercise 7"


def compute_grade(score: float) -> str | type:
    """
    Purpose:
        Takes in a float between 0 and 1 to reperesent a score and will return
        the grade that someone would have earned with that score.
    Input:
        score (float):
            The numberic score based on a percentage out of 1.00 where 0.75
            would be a C.
    Output:
        (string):
            The letter grade that someone would get ranging from A down to F
        (ValueError):
            If the score is too high (above 1.0)
    """

    if score > 1.0:
        return ValueError

    if score >= 0.9:
        return "A"
    if score >= 0.8:
        return "B"
    if score >= 0.7:
        return "C"
    if score >= 0.6:
        return "D"

    return "F"


LIMIT = 5
LEAVE = False
for attempt in range(LIMIT):
    while True:
        user_entered = input("Enter score (between 0 and 1): ")
        if isinstance(user_entered, str) and user_entered.lower() == "q":
            LEAVE = True
            break
        try:
            user_entered = float(user_entered)
        except ValueError:
            print(f"Bad input. {LIMIT - attempt - 1} tries left")
            break

        if user_entered > 1.0:
            print(f"Score too high. {LIMIT - attempt - 1} tries left")
            break

        grade = compute_grade(float(user_entered))
        print(grade)

    if LEAVE is True:
        break
