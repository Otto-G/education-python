"Chapter 3: Exercise 2"
LIMIT = 5
for attempt in range(LIMIT):
    tries_left = LIMIT - attempt - 1
    try:
        hours = int(input("Enter Hours: "))
    except ValueError:
        print(
            f"Error, please enter numeric (int) input. {tries_left} tries left."
        )
        continue
    try:
        pay = float(input("Enter Rate: "))
    except ValueError:
        print(
            f"Error, please enter numeric (float) input. {tries_left} tries left."
        )
        continue

    total_pay = hours * pay

    if hours > 40:
        hours -= 40
        total_pay += hours * pay * 0.5

    print(f"Pay: ${total_pay:.2f}")
    break
