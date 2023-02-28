"Chapter 4: Exercise 1"

import random

for i in range(5):
    print(f"Run {i} returns the value between 5 & 10: {random.randint(5, 10)}")

CHOICES = [1, 2, 3]
for i in range(2):
    print(f"Run {i} retured the choice {random.choice(CHOICES)}")
