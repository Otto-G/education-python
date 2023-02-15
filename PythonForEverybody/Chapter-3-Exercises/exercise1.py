hours = int(input("Enter Hours: "))
pay = float(input("Enter Rate: "))

totalPay = hours * pay

if hours > 40:
    hours -= 40
    totalPay += hours * pay * 0.5

print("Pay: ${:.2f}".format(totalPay))
