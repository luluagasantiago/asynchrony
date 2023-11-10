# Asynchronous Programming with asyncio in Python

I found out that the 'asyncio' library for python can run multiple tasks asynchronously making use of a single thread; I find it interesting because it appears to solve the proble of time overhead when having to deal with many threads. I made this repository to track what I learn about it.

## Overview

`asyncio` is a Python library that enables concurrent execution of tasks through the use of coroutines, `async` and `await` syntax, and an event loop. This repository serves as a guide to understanding and effectively using `asyncio` for various asynchronous operations.

## Key Features

- **Asynchronous Programming:** Learn the fundamentals of asynchronous programming using `asyncio`.
- **Event Loop:** Explore how the event loop works and how it manages asynchronous tasks.
- **Coroutines and Tasks:** Understand the concepts of coroutines, tasks, and their role in `asyncio`.
- **Concurrency and Parallelism:** Delve into the difference between concurrency and parallelism in the context of `asyncio`.
- **Best Practices and Examples:** Discover best practices and practical examples for implementing `asyncio` in different scenarios.

## summer.py
A short script to practice with aiohttp using an API from https://quantumnumbers.anu.edu.au/ to get random numbers.
 In this script we make m requests to the API in order to get the sum of n random numbers using m workers (each async call to the coroutine worker). 

## Sources
realpython.com