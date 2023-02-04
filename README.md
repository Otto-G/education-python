# Education: Python

Projects meant to learn more about python. I want to go back to some of the beginning fundamentals that I missed by diving into the deep end and fill in some of my missing knowledge.  Learning in a more structured way will help with showing the missing areas and expanding my current knowledge.  

# Topics

 - Async: Working with multiple threads and having functions return results as needed without blocking other functions from running
 - Python for Everybody: Structured learning to go over main python topics.  
 - Simple Flask Webpage: Creating a web app using flask to run python code

# Dev-Container

This code will be run in a development container for python to help keep the development environment consistent and allow for the different modules needed isolated. 

# Resources

 - [Understanding Non Blocking I/O with Python](https://medium.com/vaidikkapoor/understanding-non-blocking-i-o-with-python-part-1-ec31a2e2db9b)
    - Worked on in [Async](./Async/README.md)
 - [Python for Everybody](https://www.py4e.com/book)
    - Worked on in [PythonForEverybody](./PythonForEverybody/README.md)
 - [ ] "Think Python: How to Think Like a Computer Scientist"

# Benchmarking

## [Mandelbrot benchmark](./Mandelbrot-benchmark.py) @ 16000

Run with `> time python Mandelbrot-benchmark.py 1600 > /dev/null`

| Computer | Time m:ss | Percentage from Best | 
| :-- | --: | --: | 
| Ncase M1 - 5600x (dev container) | 1:15 | 100% | 
| Macbook Pro 14" M1-pro (dev container) | 1:17 | 103% | 
| Dell 5420 i7-1185g7 | 1:53 | 151% | 
| iPad Air 4 | 6:30 | 520% | 
