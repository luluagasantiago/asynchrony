from random import randint
import time 
import asyncio


# Generators :(Producer) sequence of any kind of values

def odds(start: int , stop: int) -> int:
    """Generator inclusive sequence"""
    for odd in range(start, stop + 1, 2):
        #yiels: return out value and then pause
        # with next(), ask the function to resume
        yield odd


# Corouritines: (Consumer) Consume values

# In order to use await, we need the function to be async
async def randn() -> int : 
    #await allows this particular function to pause
    # But other things can continue to run. 
    # We could imagine this as "running in the background"
    await asyncio.sleep(3)
    return randint(1,10)

async def main():
    odd_values = [odd for odd in odds(3,15)]
    print(odd_values)
    odds2 = tuple(odds(21,29))
    print(odds2)

    start = time.perf_counter()
    r = await randn()
    elapsed =time.perf_counter() - start
    
    print(f"{r} took {elapsed:0.2f} seconds.")

    start = time.perf_counter()
    # We gather more than one task to test the behaviour of the code 
    # wehn using asyncio tasks and the event loop
    # expected behavior: all the taks (randn) should take only 3 seconds
    r = await  asyncio.gather(*(randn() for _ in range(10)))
    elapsed =time.perf_counter() - start
    
    print(f"{r} took {elapsed:0.2f} seconds.")



#event loop: run async tasks, perform IO ops and suprocesses.
if __name__ == "__main__":
    asyncio.run(main()) 
