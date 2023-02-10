hours = int(input("Enter Hours: "))
pay = float(input("Enter Rate: "))

totalPay = hours * pay
print("Pay: ${:.2f}".format(totalPay))
