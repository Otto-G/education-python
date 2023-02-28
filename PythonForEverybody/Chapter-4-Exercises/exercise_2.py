"""Chapter 4: Exercise 2

This program will give a NameError when run because repeat_lyrics() hasn't been
defined yet.  
"""

repeat_lyrics()  # type: ignore


def print_lyrics():
    "Tell people that you're a lumberjack"

    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")


def repeat_lyrics():
    "Print the lyrics twice"

    print_lyrics()
    print_lyrics()
