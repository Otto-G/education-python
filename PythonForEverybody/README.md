# Major Goal of [Book](https://www.py4e.com/book)

The book is similar to *"Think Python: How to Think Like a Computer Scientist"* but it more focused on data compared to algorithms and abstractions.  Since there is more focus on data science, there is still more that can be learned from the *"Think Python"* book if more knowledge is wanted. 

My goal is to reinforce some of the fundamentals that I skipped when I dove into the deep end at work getting a large (12,000 lines) program running.  I learned a lot during that process, but I've found that some fundamentals have been missed and I've relied on searching for how to do things instead of knowing how to do them.  

# Notes

## Chapter 1: Why should you learn to write programs?

This chapter is mostly about what programming is and the introductory basics of how the syntax works.  There are bits about how to install python and how to run "Hello World" as well as how to quit the terminal interpreter.  

There is a bit that goes over the differences between high level languages like Python, Javascript, Ruby, etc. and machine language.  The main feature of the high level languages is that they are able to be run on different sets of hardware without change because of interpreters in the middle that are able to create the machine code needed to run it on the specific system that it is actually used on.  There is a difference between interpreters that read the source code of a program and executes them on the fly and a compiler that need to have the whole program as one file which can then generate machine language code which can be run.  

Errors will pop up while programming and it is important to distinguish between: 

 - **Syntax Errors**: Errors that go against the rules of Python and cause an error during the runtime.  
 - **Logic Errors**: Errors that don't prevent the program from running, but do tasks in the wrong order and will create bad results.  
 - **Semantic Errors**: Errors that don't prevent the program from running and will appear to work correctly, but have wrong instructions (turn right instead of left)

Debugging will need to be done to fix the errors.  There are four main things that can be tried to solve whatever issue there is:

 - **Reading**: Looking at the code and reading it back to yourself to see if it matches what you wanted it to say.  
 - **Running**: Make changes to the code and run it to see if it will display a helpful error that is more obvious than the first one.  This might require adding in some extra code like logging or printing to the terminal.  
 - **Ruminating**: Taking some time to think about what type of error you're dealing with and what information you can get from the error messages.  What changes have been applied since it was last working and what areas could be impacted.  
 - **Retreating**: Undo some changes and get it back to a working state.  From there it is possible to rebuild on a more solid foundation.  

 Beginners often get stuck on thinking of one type of process instead of trying to use the other ones.  Sometimes it might be best to keep breaking the code down into smaller blocks so it can be easier to find errors and then fix them.  

 The learning process is a journey.  It is ok if it takes time to really grasp the different concepts and commit them to memory.  It can take time to go from just understanding the basics to writing full and complex programs.  

 ## Chapter 2: Variables, expressions, and statements

 **Variables** are words that hold a value in Python.  They can't start with numbers or contain illegal characters like "@" or use Python's list of reserved keywords...

| <!-- --> | <!-- -->| <!-- --> | <!-- --> | <!-- --> | 
| ---      | ---     | ---      | ---      | ---      | 
| and      | del     | from     | None     | True     | 
| as       | elif    | global   | nonlocal | try      | 
| assert   | else    | if       | not      | while    | 
| break    | except  | import   | or       | with     | 
| class    | False   | in       | pass     | yield    |
| continue | finally | is       | raise    | async    | 
| def      | for     | lambda   | return   | await    | 

**Statements** are lines of code that python can execute. 

**Operators** are the mathematical symbols that can be used such as "+, -, *, /, and \*\*".  A list of operators can be found on [the python doc page](https://docs.python.org/3/library/operator.html#mapping-operators-to-functions).  The modulus "%" operator can be fairly useful since it will return the remainder after the first number has been divided by the second number.  This can identify numbers that are divisible by each other when the remainder is 0.  **Operands** are what the functions are being applied to.  

**Expressions** is a combination of values, variables, and operators.  Expressions will be evaluated and displayed while using an interactive terminal, but won't do anything in a script since the only output from a script must be explicitly called.  

Python follows *PEMDAS* for **Order of Operations** as that is the mathematical convention.  Parentheses should be added if there is any question about the order of operations as well as to help with readability.  

Strings can also have some mathematical operations applied to them such as "+" which will concatenate two strings together or "\*" which will multiply the string by however number of times.  

The input function can be used to get a user input and will resume the code when the user presses the enter button.  A string can be added in the middle of the function to have some text describe what is being prompted for.  