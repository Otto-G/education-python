# Major Goal of [Book](https://www.py4e.com/book)

The book is similar to *"Think Python: How to Think Like a Computer Scientist"*
but it more focused on data compared to algorithms and abstractions.  Since
there is more focus on data science, there is still more that can be learned
from the *"Think Python"* book if more knowledge is wanted.

My goal is to reinforce some of the fundamentals that I skipped when I dove into
the deep end at work getting a large (12,000 lines) program running.  I learned
a lot during that process, but I've found that some fundamentals have been
missed and I've relied on searching for how to do things instead of knowing how
to do them.

## Chapter 1: Why should you learn to write programs?

This chapter is mostly about what programming is and the introductory basics of
how the syntax works.  There are bits about how to install python and how to run
"Hello World" as well as how to quit the terminal interpreter.  

There is a bit that goes over the differences between high level languages like
Python, Javascript, Ruby, etc. and machine language.  The main feature of the
high level languages is that they are able to be run on different sets of
hardware without change because of interpreters in the middle that are able to
create the machine code needed to run it on the specific system that it is
actually used on.  There is a difference between interpreters that read the
source code of a program and executes them on the fly and a compiler that need
to have the whole program as one file which can then generate machine language
code which can be run.  

Errors will pop up while programming and it is important to distinguish between:

- **Syntax Errors**: Errors that go against the rules of Python and cause an
error during the runtime.  
- **Logic Errors**: Errors that don't prevent the program from running, but do
tasks in the wrong order and will create bad results.  
- **Semantic Errors**: Errors that don't prevent the program from running and
will appear to work correctly, but have wrong instructions (turn right instead
of left)

Debugging will need to be done to fix the errors.  There are four main things
that can be tried to solve whatever issue there is:

- **Reading**: Looking at the code and reading it back to yourself to see if it
  matches what you wanted it to say.  
- **Running**: Make changes to the code and run it to see if it will display a
  helpful error that is more obvious than the first one.  This might require
  adding in some extra code like logging or printing to the terminal.  
- **Ruminating**: Taking some time to think about what type of error you're
  dealing with and what information you can get from the error messages.  What
  changes have been applied since it was last working and what areas could be
  impacted.  
- **Retreating**: Undo some changes and get it back to a working state.  From
  there it is possible to rebuild on a more solid foundation.  

Beginners often get stuck on thinking of one type of process instead of trying
to use the other ones.  Sometimes it might be best to keep breaking the code
down into smaller blocks so it can be easier to find errors and then fix them.  

The learning process is a journey.  It is ok if it takes time to really grasp
the different concepts and commit them to memory.  It can take time to go from
just understanding the basics to writing full and complex programs.  

## Chapter 2: Variables, expressions, and statements

 **Variables** are words that hold a value in Python.  They can't start with
 numbers or contain illegal characters like "@" or use Python's list of reserved
 keywords...

| <!-- --> | <!-- --> | <!-- --> | <!-- --> | <!-- --> |
| ---      | ---      | ---      | ---      | ---      |
| and      | del      | from     | None     | True     |
| as       | elif     | global   | nonlocal | try      |
| assert   | else     | if       | not      | while    |
| break    | except   | import   | or       | with     |
| class    | False    | in       | pass     | yield    |
| continue | finally  | is       | raise    | async    |
| def      | for      | lambda   | return   | await    |

**Statements** are lines of code that python can execute.

**Operators** are the mathematical symbols that can be used such as "+, -, *, /,
and \*\*".  A list of operators can be found on [the python doc
page](https://docs.python.org/3/library/operator.html#mapping-operators-to-functions).
The modulus "%" operator can be fairly useful since it will return the remainder
after the first number has been divided by the second number.  This can identify
numbers that are divisible by each other when the remainder is 0.  **Operands**
are what the functions are being applied to.  

**Expressions** is a combination of values, variables, and operators.
Expressions will be evaluated and displayed while using an interactive terminal,
but won't do anything in a script since the only output from a script must be
explicitly called.  

Python follows *PEMDAS* for **Order of Operations** as that is the mathematical
convention.  Parentheses should be added if there is any question about the
order of operations as well as to help with readability.  

Strings can also have some mathematical operations applied to them such as "+"
which will concatenate two strings together or "\*" which will multiply the
string by however number of times.  

The input function can be used to get a user input and will resume the code when
the user presses the enter button.  A string can be added in the middle of the
function to have some text describe what is being prompted for.  

Comments can be added in python by using the "#" mark.  This can be used either
at the beginning of a line or towards the end of one since everything after the
"#" will be ignored.  It can be good to let the code speak for itself when it
can and use comments to describe why a bit of code is doing what it is doing.
That also means that the code needs to be structured so that it easy to read and
understand.  Using mnemonic variable names will help aid in making the code
readable from the start while comments can fill in the gaps of why is has been
done the way it has.  

## Chapter 3: Conditional Execution

Conditionals start by using different comparison operators and return either
`True` or `False`.  

| Code       | Meaning                         |
| ---------- | ------------------------------- |
| x == y     | x is equal to y                 |
| x != y     | x is **not** equal to y         |
| x > y      | x is greater than y             |
| x < y      | x is less than y                |
| x >= y     | x is greater than or equal to y |
| x <= y     | x is less than or equal to y    |
| x is y     | x is the same as y              |
| x is not y | x is **not** the same as y      |

\* Note that there is a slight difference between `==` and `is`.  `==` will
compare the values, but `is` will compare the whole object.  

These conditionals can be combined by using `and`, `or`, and `not`.  The meaning
and usage of them is the same as standard English.  

As many functions end up needing some form of logic to process information,
these conditional statements are often used in `if` statements.  They have the
below structure:

```python
if x > 0:
    print('x is positive')
```

The `if` command is followed by a conditional of some kind and then ended with a
colon `:`.  From there, the next line needs to be indented along with any other
line that is intended to be included in the `if` statement.  This structure is
the same as `for` loops.  `pass` can be used along with a comment if the logic
is just being implemented but the code isn't finished yet.  

`if` statements can be extended with alternate executions by using `else` or
additional conditions can be chained by using `elif`.  `elif` is a shorter
notation of "else if".  The `elif` commands can only be after the initial `if`
command and `else` commands can only be at the end of a string of conditionals.
The conditions will always be checked in order and once one is true, the rest
will be ignored.  The conditionals can also be nested as many times as desired
but that can start to become difficult to read.  Ideally, code is kept to 3
indentations or less.  

```python
if x > 0:
    print('x is positive')
elif x == 0:
    print('x is 0')
else:
    print('x is negative')
```

The above `elif` statement will only be run if `x <= 0` and the `else` statement
will only run if `x < 0`.  

### Catching Exceptions

When functions are created, they can often throw errors if the wrong inputs are
given.  This isn't really a concern when working in a live interpreter, but when
a script is being created, this can cause issues.  `try` and `except` are
conditionals that are in python to allow the ability to catch errors and deal
with them.  The are best used for user input areas to ensure valid inputs or for
calling external resources that might return unexpected values.  

### Short-circuit Evaluation of Logical Expressions

As python evaluates statements from left to right, if there is an `and`
statement where the first conditional is `False`, the second (or more)
conditional(s) will be discarded.  This can lead to *guardian patterns* where
the first statement will block execution of a second (or more) statement.  The
below code prevents an error from being thrown because `y` is confirmed to be a
0 before it can be used in a division throwing a `ZeroDivisionError`.  

```python
x = 1
y = 0
x >= 2 and y != 0 and (x/y) > 2

False
```

## Chapter 4: Functions

Functions are series of commands that perform some kind of computation.  When a
funciton is defined the name and the arguments that are needed in order to
perform the computation.  

There are several built-in functions in python that can be used.  Those built in
functions should be treated as reserved words and shouldn't be used.  

| Function | Action |
| -------- | ------ |
| int()    | Takes strings or floats and turns them into ints.  Note that it just chops off the end of the number instead of rounding |
| float()  | Converts strings or ints into floating point numbers |
| str()    | Converts it's arguments into a string |

There is also a built in math module that needs to be imported in order to work
by adding `import math` to the beginning of the python file.  This will create a
module that is able to be used to perform different functions like
`math.log10()` or `math.sin(math.pi)`.

Generally it is wanted for computer programs to return the same result every
time that the program is run making it *determininistic*.  This is normally
good, but sometimes it is desired to have *nondetermininistic* results by
intruducing some randomness.  Computers have a hard time actually generating
real random numbers, but they can generate *pseudorandom* numbers.  Python uses
the built in module that needs to be imported `random` to do this.  There are
multiple functions within this module that can be used to create random data.
