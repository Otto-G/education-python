# Major Goal of [Book](https://www.py4e.com/book)

The book is similar to *"Think Python: How to Think Like a Computer Scientist"* but it more focused on data compared to algorithms and abstractions.  Since there is more focus on data science, there is still more that can be learned from the *"Think Python"* book if more knowledge is wanted. 

My goal is to reinforce some of the fundamentals that I skipped when I dove into the deep end at work getting a large (12,000 lines) program running.  I learned a lot during that process, but I've found that some fundamentals have been missed and I've relied on searching for how to do things instead of knowing how to do them.  

# Notes

## Chapter 1: Why should you learn to write programs?

This chapter is mostly about what programming is and the introductory basics of how the syntax works.  There are bits about how to install python and how to run "Hello World" as well as how to quit the terminal interpreter.  

There is a bit that goes over the differences between high level languages like Python, Javascript, Ruby, etc. and machine language.  The main feature of the high level languages is that they are able to be run on different sets of hardware without change because of interpreters in the middle that are able to create the machine code needed to run it on the specific system that it is actually used on.  There is a difference between interpreters that read the source code of a program and executes them on the fly and a compiler that need to have the whole program as one file which can then generate machine language code which can be run.  

Errors will pop up while programming and it is important to distinguish between 

 - **Syntax Errors**: Errors that go against the rules of Python and cause an error during the runtime.  
 - **Logic Errors**: Errors that don't prevent the program from running, but do tasks in the wrong order and will create bad results.  
 - **Semantic Errors**: Errors that don't prevent the program from running and will appear to work correctly, but have wrong instructions (turn right instead of left)