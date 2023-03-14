"Chapter 4: Exercise 6"


def compute_pay(hours: float, rate: float) -> float:
    """
    Purpose:
        Takes two arguments, hours and rate, and will comput the amount that
        someone is to be paid based on a standard 40 hour work week.  If the
        hours work exceed 40, they will be paid time and a half.
    Input:
        hours (float):
            The whole number of hours worked
        rate (float):
            The amount that someone is to be paid per hour
    Output:
        total_pay (float):
            The total amount to be paid to someone
    """

    total_pay = hours * rate

    if hours > 40:
        hours -= 40
        total_pay += hours * rate * 0.5

    return total_pay


LIMIT = 5
for attempt in range(LIMIT):
    tries_left = LIMIT - attempt - 1
    try:
        hours_worked = float(input("Enter Hours: "))
    except ValueError:
        print(f"Error, please enter numeric (int) input. {tries_left} tries left.")
        continue
    try:
        pay_rate = float(input("Enter Rate: "))
    except ValueError:
        print(f"Error, please enter numeric (float) input. {tries_left} tries left.")
        continue

    pay = compute_pay(hours_worked, pay_rate)

    print(f"Pay: ${pay:.2f}")
    break
