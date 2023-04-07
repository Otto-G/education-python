"""
Chapter 6: Exercise 1

Write a while loop that starts at the last character in the string and works its
way backwards to the first character in the string, printing each letter on a
separate line, except backwards.
"""


def reverse_print(string: str) -> None:
    """
    Purpose
        Take a string and print it in reverse order
    """
    index = len(string)

    while index > 0:
        index -= 1
        print(string[index])


reverse_print("Fruit")
