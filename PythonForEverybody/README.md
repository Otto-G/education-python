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
|----------|----------|----------|----------|----------|
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
|------------|---------------------------------|
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
function is defined the name and the arguments that are needed in order to
perform the computation.  

### Built-in functions

There are several built-in functions in python that can be used.  Those built in
functions should be treated as reserved words and shouldn't be used.  

### Type conversion functions

| Function | Action                                                                                                                     |
|----------|----------------------------------------------------------------------------------------------------------------------------|
| int()    | Takes strings or floats and turns them into an int.  Note that it just chops off the end of the number instead of rounding |
| float()  | Converts strings or int into floating point numbers                                                                        |
| str()    | Converts it's arguments into a string                                                                                      |

### Math functions

There is also a built in math module that needs to be imported in order to work
by adding `import math` to the beginning of the python file.  This will create a
module that is able to be used to perform different functions like
`math.log10()` or `math.sin(math.pi)`.

### Random numbers

Generally it is wanted for computer programs to return the same result every
time that the program is run making it *deterministic*.  This is normally
good, but sometimes it is desired to have *nondeterministic* results by
introducing some randomness.  Computers have a hard time actually generating
real random numbers, but they can generate *pseudorandom* numbers.  Python uses
the built in module that needs to be imported `random` to do this.  There are
multiple functions within this module that can be used to create random data.

### Adding new functions

While mostly built-in functions have been used so far.  It is also possible to
define new functions that can be used.  A *function definition* specifies the
name of a new function and the sequence of statements that are executed when
that function is called.  This helps to reduce code duplication

Example:

```python
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")
```

`def` is a keyword that indications that a new function is going to be defined.
It will be followed by the name of the function, in this case `print_lyrics`.
Within the `()` the required arguments can be defined as needed but the is no
need to require any if they aren't needed like in this case.  The first line of
the function definition is called the *header* and the rest is called the
*body*.  The *header* **must** end with a colon and the *body* **must** be
indented.  The general convention is to use 4 spaces for indentation.  The
function will stop being defined when there are no more lines or there is
another line that is un-indented.  

Functions can be defined in Python's interactive mode where it will change from
`>>>` to `...` in order to indicate that the definition isn't complete.  The way
to end the function in Python's interactive mode is by entering an empty line.

As Python is an object oriented language, when creating a new function, it will
also be a variable (object) with the name of the function.  The syntax for
calling the function is the same for the built-in functions where the previous
function can be called by calling `print_lyrics()`.  Since it can be called, it
can also be included in other functions like so...

```python
def repeat_lyrics():
    print_lyrics()
    print_lyrics()
```

### Definitions and uses

To put the two code fragments together they would look like...

```python
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()
```

This code defines two functions and the order of the definition matters.  In
order for a function to be called, it must first be defined.  The code inside
won't be run until it is called, but the definition must exist first.

### Flow of execution

The flow of execution is essential to understand since that is the only way to
know how your program will run.  Python programs will always execute from the
first line down, but function definitions will cause the lines inside of them to
be skipped.  This is important to know for being able to read the code as well
as structuring it since reading strictly from the top down might not make sense
if the function definitions aren't all lined up in how they are executed in the
actual program.  

### Parameters and arguments

Functions are called using arguments sometimes like `math.pow(2, 3)` which is
taking two arguments.  Those arguments are then passed into the function and
assigned to variables called parameters.  

```python
def print_twice(bruce):
  print(bruce)
  print(bruce)
```

Here this function takes one argument and assigns it to the variable `bruce`.
Whenever the function is called, it will print out the value of the parameter
twice no matter what it is so long as it can be printed.

```python
>>> print_twice(17)
17
17
>>> import math
>>> print_twice(math.pi)
3.141592653589793
3.141592653589793
```

We can still use the standard rules of composition by using any kind of
expression as an argument for the function like...

```python
>>> print_twice(math.cos(math.pi))
-1.0
-1.0
```

The argument will be evaluated before the function is called so the expression
`math.cos(math.pi)` is only evaluated once.  You can also use variables as
arguments.  The name of the variable that is being passed into the function has
no impact to the variables inside of the function.  The variable will be
assigned to whatever parameter the function has defined it to be.  Outside
variables do not exist within functions (except for `Class` variables).  

### Fruitful functions and void functions

Some functions like math functions will yield results and could be described as
fruitful functions for this book.  Other functions just perform an action like
`print()` and then exit without returning a value.  Normally when a function
will return a value, it will be used later on as a new variable.  

```python
x = math.cos(math.pi)
```

WHen a function is called in an interactive window, the result will be
displayed, but in a script nothing will happen unless the result is stored.
Void functions might display something or have other effect, but they don't have
any return value.  If you try to assign the result to a variable, it will only
store none.  

```python
>>> x = print_twice(5)
5
5
>>> print(x)
None
```

From [Chapter 2](#chapter-2-variables-expressions-and-statements), None is a
special type.  Creating a function that will return a value requires the use of
an aptly named `return` statement.  A basic function that would return the value
of two numbers added together could look like this.  

```python
def add_two(a, b):
  added = a + b
  return added

x = add_two(3, 5)
print(x)
```

If the above script is run, it will print out 8 because x was assigned the value
of 8 from the return of the `add_two` function.  The `add_two` function took the
arguments 3 and 5 which were added together and then passed to a `return`
statement.  

### Why functions

Functions have several uses

- Creating functions helps to bundle statements making the program easier to
  read and debug
- Functions can eliminate duplicate code since it can exist in one place and be
  run many times.  This also makes debugging or changing code easier since the
  code will only need to be changed in one location.
- Dividing a long program into functions makes it possible to debug or test one
  section at a time and then assemble the all of the functions into one working
  piece.  
- Well designed functions are often useful for many programs.  Once they have
  been written and debugged, it can be reused in other programs.  

## Chapter 5: Iteration

### 5.1 Updating variables

It is common to want to update a variable based on it's existing value such as
`x = x + 1`.  In order for this statement to work in Python, `x` must already
exist since it is required to be known in order to calculate the new value.
This can be done by first assigning a value to it such as:

```python
x = 0
x = x + 1
x += 1
```

### 5.2 The `while` statement

Since doing repetitive tasks is something that computers do very well, python
has several features to make it easier.  

One form is using `while` statements.  They will continue to run so long as the
statement following `while` is true.  See the example code block:

```python
n = 5
while n > 0:
  print(n)
  n -= 1
print("Blastoff")
```

It is possible to mostly read while statements like standard English.  Just like
`if` statements, the code that is run within the loop must be indented.  For
this example, it sets `n` to 5 and then evaluates if it is greater than 0.
Since this returns true, it will print the value and subtract 1.  From there it
returns to the beginning and evaluates if `n` (now 4) is greater than 0.  This
pattern continues until `n=0` and the `while` statement returns false.  At that
point it goes to the next un-indented line and prints out "Blastoff".  

Every time that the `while` statement is evaluated is a new iteration and every
time that it returns to the initial `while` statement is a loop.  It is
important to make sure that there is an end to the loop by some variable that
will change every loop which will make the `while` statement return false.  The
variable that is changed can be called the *iteration* variable.  If there is no
*iteration variable* or some other signal that will eventually cause an exit,
the loop will be an *infinite loop*

### 5.3 Infinite loops

Infinite loops will go on forever unless there is a `break` statement called in
the middle of the loop somewhere.  Code such as:

```python
n = 10
while True:
  print(n, end=" ")
  n -= 1
print("Done!")
```

Will run forever and never exit until the program is manually terminated
somehow.  Ctrl+C or closing the program are the two main ways to manually close
programs that have ended up going on with no end.  Building infinite loops with
ways to end the loop can be useful.  

```python
while True:
  line = input("> ")
  if line == "done":
    break
  print(line)
print("Done!")
```

This code will ask for user input until the word "done" is typed in.  When the
word "done" is typed in, the `if` statement will return as `True` and then break
out of the loop.  

### 5.4 Finishing iterations with `continue`

Sometimes it might be desired to immediately end an iteration based on some
condition and immediately start a new iteration.  The statement to do this is
`continue`. When `continue` is passed, the iteration will immediately stop and
loop back to the start of the loop.

```python
while True:
  line = input("> ")
  if line[0] == "#":
    continue
  if line == "done":
    break
  print(line)
print("Done!")
```

This code will run forever and echo out the input unless the input starts with
`#` where that will be skipped and another input will be requested.  

### 5.5 Definite loops using `for`

If there is a need to loop through a list of things, using a `for` loop can be a
better option.  These are called *definite* loops since the loop will last only
as long as the list of things to iterate through.  

```python
friends = ["Joseph", "Glenn", "Sally"]
for friend in friends:
  print("Happy New Year:", friend)
print("Done!")
```

As this example shows, the syntax for a `for` loop is very similar to a `while`
loop. This example created a list of `friends` and then for every iteration of
the `for` loop, one of the friends would be assigned to the variable `friend`
starting at `friends[0]` or "Joseph" and going until all of the `friends` had
gone through the loop.  This takes 3 loops to accomplish in total.  

It is important to note that `for` and `in` are reserved words in python.  `for`
designates that a loop will be made and `friend` is the *iteration variable*
that will iterate through the different elements `in` `friends`.  

### 5.6 Loop patterns

Normally loops are used when there is a desire to go through a list of items or
the contents of a file.  The loops are generally started by:

- Initializing one or more variables before the loop starts
- Performing some computation on each item in the loop body, possibly changing
the variables in the body of the loop
- Looking at the resulting variables when the loop completes

#### 5.6.1 Counting and summing loops

To count the number of items in a list a `for` loop can be used

```python
count = 0
for iter_var in [3, 41, 12, 9, 74, 15]:
  count += 1

print("Count: ", count)
```

The statement is initialized with `count = 0` so that the variable exists and
the starting value is 0.  iter_var is the *iteration* variable that is used to
iterate through the loop.  The value that it is stored as (the values in the
list) isn't being used in the code but it is available in the body of the `for`
loop.  The body of the `for` loop is just using the `count` variable and adding
1 to it each loop.  Once the loop is finished, the final value of `count` is
printed out.  

A similar loop that would find the total of all of the values in the list would
look like:

```python
total = 0
for iter_var in [3, 41, 12, 9, 74, 15]:
  total += iter_var

print(f"Total = {total}")
```

This example uses the `iteration variable`, `iter_var`, by adding it's value to
total which was defined outside of the loop body so that there wouldn't be an
error when it was added to within the body.  These code snippets aren't very
useful since the built in `len()` and `sum()` are able to perform the same
function.  In general it is best to rely on the builtin functions of python
since they have had more optimization applied to them than creating a new method
of doing something routine.  

#### 5.6.2 Maximum and minimum loops

To find the largest value in a list we can create a loop like so:

```python
largest = None
print(f"Before: {largest}")
for i, iter_var in enumerate([3, 41, 12, 9, 74, 15]):
  # enumerate will return the position as well as the value of a list in a for 
  # loop.  The first value will indicate the position/loop number and iter_var 
  # will be the value at that point.  

  if largest is None or iter_var > largest:
    # this will run only if either largest is None or if the current iter_var
    # is more than the current largest value we have seen.  Since the list 
    # starts with 3, largest will first be assigned to 3 and then when 41 shows 
    # up next that will be greater than 3 so largest will be reassigned.  The 
    # next value 12 is less than 41 so largest will not be assigned.  

    largest = iter_var
  print(f"Loop {i}: iter_var = {iter_var}: largest = {largest}")
print(f"Largest = {largest}")
```

The variable `largest` can be thought of as the largest value that has been seen
up until that point in time.  Before the loop, the value is set to `None` which
is a special value that is the same as "empty".  

Changing this code to find the smallest only takes one small change (also
changing the variable names for clarity).

```python
smallest = None
print(f"Before: {smallest}")
for i, iter_var in enumerate([3, 41, 12, 9, 74, 15]):
  if smallest is None or iter_var < smallest:
    # The only real change here is changing the greater than sign for a less 
    # than sign.  The logic is otherwise the exact same.  

    smallest = iter_var
  print(f"Loop {i}: iter_var = {iter_var}: smallest = {smallest}")
print(f"Smallest = {smallest}")
```

These bits of code are also not needed since Python has built-in `max()` and
`min()` functions that make hand writing loops unnecessary.  A simple version of
the Python built-in `min()` function would look like:

```python
def min(values):
  smallest = None
  for value in values:
    if smallest is None or value < smallest:
      smallest = value
  return smallest
```

The `print()` statements have been removed and since there isn't a desire to
print out the loop number, enumerate has also been removed.  

#### 5.7 Debugging

As you start writing larger and larger programs, there is probably going to be a
need to spend more time debugging.  More code means that there are more chances
for an error to pop up.  One way of debugging instead of going line by line
which can become excessive is to start in the middle.  This way you can know if
there is an error in the first half or the second half of your program.  This
process can be repeated until you are able to narrow down the cause of the
error.  In theory, this would reduce a maximum 100 step process into a maximum 6
step process.  

It isn't always clear where the middle point is or even if it's possible to
check there, but this gives a process that is better than going line by line.  

#### 5.8 Glossary

- **accumulator** A variable used in a loop to add up or accumulate a result.
- **counter** A variable used in a loop to count the number of times something
    happened. We initialize a counter to zero and then increment the counter
    each time we want to “count” something.
- **decrement** An update that decreases the value of a variable.
- **initialize** An assignment that gives an initial value to a variable that
  will be updated.
- **increment** An update that increases the value of a variable (often by one).
- **infinite loop** A loop in which the terminating condition is never satisfied
  or for which there is no terminating condition.
- **iteration** Repeated execution of a set of statements using either a
  function that calls itself or a loop.

## Chapter 6: Strings

### 6.1 A string is a sequence

A string is a *sequence of characters.  Using a bracket operator, it is possible
to access characters by their location.

```python
>>> fruit = "banana"
>>> letter = fruit[1]
>>> print(letter)
a
```

The second statement in the above code extracts the letter at index position 1
and assigns that value to letter.   Note that Python uses zero indexing so index
position 0 would return "b".  

#### 6.2 Getting the length of a string using `len`

`len` is a built-in function that returns the number of characters in a string.

```python
>>> fruit = "banana"
>>> len(fruit)
6
```

To get the last letter of a string it might be tempting to use
`last = fruit[len(fruit)]` but that would result in an `IndexError` since the
length of the variable is one larger than the index value.  To get the last
letter it would be needed to subtract 1 from the result like
`last = fruit[len(fruit)-1]`.  

An alternative option would be to use native indices which count backward from
the end.  `fruit[-1]` would yield the last letter while `fruit[-2]` would yield
the second to last letter.  

#### 6.3 Traversal through a string with a loop

There can be many reasons to process a string one character at a time.  They
would normally start at the beginning, select each character and do something
and repeat until the end.  This is called a *traversal*.  One way to write a
*traversal* is by using a `while` loop:

```python
index = 0
fruit = "banana"
while index < len(fruit):
  letter = fruit[index]
  print(letter)
  index += 1
```

This loop will traverse the variable `fruit` until the index is the same as the
length of the variable `fruit`.  The last character printed here would be
`fruit[len(fruit)-1]` because the index is incremented after the call.  

Another way to write a traversal loop is by using a `for` loop:

```python
for char in fruit:
  print(char)
```

Each time through the loop, the next character in the string will be assigned to
the variable `char` and it will continue until there are no characters left.  

#### 6.4 String slices

Strings can be spit into a segment called a *slice*.  Selecting them is similar
to selecting a character but a range is given instead of a single index.  

```python
>>> string = 'Monty Python'
>>> print(string[0:5])
Monty
>>> print(string[6:12])
Python
```

The operator `[n:m]` returns the string that starts at the n-th character to the
m-th character including the first, but excluding the last.  If the first index
is omitted then the slice will stat at the beginning of the string but if the
second is omitted then it will continue to the end.  

```python
>>> fruit = 'banana'
>>> fruit[:3]
'ban'
>>> fruit[3:]
'ana'
```

If the first index is greater than or equal to the second, the result is an
*empty* string represented by two quotation marks:

```python
>>> fruit = 'banana'
>>> fruit[3:3]
''
```

An empty string has no length and contains no characters but other than that it
is the same as any other string.

#### 6.5 Strings are immutable
