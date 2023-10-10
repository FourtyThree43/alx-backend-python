# alx-backend-python

- Python Back-end

## 0x02. Python - Async Comprehension

This module is about Python's asynchronous comprehensions and generators, which allow you to write asynchronous code in Python. This is part of Python's asynchronous I/O system.

## Resources

- [PEP 530 – Asynchronous Comprehensions](https://peps.python.org/pep-0530/)
- [What’s New in Python: Asynchronous Comprehensions / Generators](https://www.blog.pythonlibrary.org/2017/02/14/whats-new-in-python-asynchronous-comprehensions-generators/)
- [Type-hints for generators](https://stackoverflow.com/questions/42531143/how-to-type-hint-a-generator-in-python-3)

## Learning Objectives

- **How to write an asynchronous generator**: An asynchronous generator is a special kind of generator that can pause execution, allowing other code to run in the meantime. It's created using `async def` and can contain `yield` expressions¹. For example:
    ```python
    async def asyncgen():
        yield 'Hello,'
        yield 'world!'
    ```
- **How to use async comprehensions**: Async comprehensions are a way to create collections (like lists, sets, dicts) based on existing iterables, but in an asynchronous manner⁶. They are only allowed inside an `async def` function⁷. For example:
    ```python
    result = [i async for i in aiter() if i % 2]
    ```
- **How to type-annotate generators**: Type annotations help specify the type of values generators can yield or return[^10^]. For example, a generator function that yields integers would be annotated as follows:
    ```python
    from typing import Generator

    def count_up_to(n: int) -> Generator[int, None, None]:
        i = 0
        while i < n:
            yield i
            i += 1
    ```

## Requirements

All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7). Please ensure that your code is compatible with this version of Python.


                          +-+-+-+-+-+-+-+-+-+-+-+-+-+
                          |F|o|u|r|t|y|T|h|r|e|e|4|3|
                          +-+-+-+-+-+-+-+-+-+-+-+-+-+
                                                         
                         _|            _|  _|  _|_|_|    
                       _|_|  _|    _|  _|  _|        _|  
                         _|    _|_|    _|_|_|_|  _|_|    
                         _|  _|    _|      _|        _|  
                         _|  _|    _|      _|  _|_|_|    
                                                         
                                                         
## ❝ Quote ❞

```
She can kill all your files;
She can freeze with a frown.
And a wave of her hand brings the whole system down.
And she works on her code until ten after three.
She lives like a bat but she's always a hacker to me.
                           -- Apologies to Billy Joel

```