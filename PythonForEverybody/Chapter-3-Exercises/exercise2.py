limit = 5
for attempt in range(limit):
    triesLeft = limit - attempt - 1
    try:
        hours = int(input("Enter Hours: "))
    except ValueError:
        print(f"Error, please enter numeric (int) input. {triesLeft} tries left.")
        continue
    try:
        pay = float(input("Enter Rate: "))
    except ValueError:
        print(f"Error, please enter numeric (float) input. {triesLeft} tries left.")
        continue

    totalPay = hours * pay

    if hours > 40:
        hours -= 40
        totalPay += hours * pay * 0.5

    print("Pay: ${:.2f}".format(totalPay))
    break
