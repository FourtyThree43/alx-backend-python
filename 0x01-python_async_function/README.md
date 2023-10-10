# alx-backend-python

## 0x00. Python - Async

This repository is about Python's async and await keywords, which allow you to write asynchronous code in Python. This is part of Python's asynchronous I/O system.

## Resources

- [asyncio - Asynchronous I/O Docs](https://docs.python.org/3/library/asyncio.html)
- [asyncio - asyncio Tutorial](https://realpython.com/async-io-python/)
- [random.uniform](https://docs.python.org/3/library/random.html#random.uniform)

## Learning Objectives

- **async and await syntax**: The `async` and `await` keywords are used in Python to write asynchronous code. The `async` keyword is used to declare a function as a coroutine²⁴. The `await` keyword is used to pause the execution of the coroutine until it completes and returns the result data²⁴. For example, you can use `await asyncio.sleep()` to pause a coroutine for a specified amount of time¹.

- **Execute an async program with asyncio**: To run an async program, you can use the `asyncio.run()` function. This function takes a coroutine as an argument, creates a new event loop, runs the given coroutine, closes the loop, and returns the result⁸. For example:
    ```python
    import asyncio

    async def main():
        print('Hello')
        await asyncio.sleep(1)
        print('world')

    asyncio.run(main())
    ```
- **Run concurrent coroutines**: To run multiple coroutines concurrently, you can use tasks. A task is a wrapper for a coroutine that schedules it to run on the event loop as soon as possible¹⁵. You can create tasks using `asyncio.create_task()` or `asyncio.ensure_future()`, and then use `asyncio.gather()` or `asyncio.wait()` to run these tasks concurrently[^10^]¹³.

- **Create asyncio tasks**: To create a task in asyncio, you can use the `asyncio.create_task()` function. This function takes a coroutine as an argument and schedules it to run on the event loop, returning a Task object¹⁵. For example:
    ```python
    import asyncio

    async def my_coroutine():
        # Coroutine body here

    task = asyncio.create_task(my_coroutine())
    ```
- **Use the random module**: The random module in Python provides functions to generate random numbers and select random elements from sequences¹⁹. For example, you can use `random.randint(a, b)` to generate a random integer between `a` and `b`, or `random.choice(sequence)` to select a random element from a sequence¹⁹.

## Requirements


- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7). Please ensure that your code is compatible with this version of Python.

```
                          +-+-+-+-+-+-+-+-+-+-+-+-+-+
                          |F|o|u|r|t|y|T|h|r|e|e|4|3|
                          +-+-+-+-+-+-+-+-+-+-+-+-+-+
                                                         
                         _|            _|  _|  _|_|_|    
                       _|_|  _|    _|  _|  _|        _|  
                         _|    _|_|    _|_|_|_|  _|_|    
                         _|  _|    _|      _|        _|  
                         _|  _|    _|      _|  _|_|_|    
                                                         
```

## ❝ Quote ❞

