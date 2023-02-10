width = 17
height = 12.0

print("width = {} \nheight = {}".format(width, height))

ans = width // 2  # Guess is 8 of type int()
print("1. width // 2 = {} of type {}".format(ans, type(ans)))

ans = width / 2.0  # Guess is 8.5 of type float()
print("2. width / 2.0 = {} of type {}".format(ans, type(ans)))

ans = height / 3  # Guess is 4 of type float()
print("3. height / 3 = {} of type {}".format(ans, type(ans)))

ans = 1 + 2 * 5  # Guess is 11 of type int()
print("4. 1 + 2 * 5 = {} of type {}".format(ans, type(ans)))
