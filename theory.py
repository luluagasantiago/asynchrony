from random import randint
import time 
import asyncio


# Generators :(Producer) sequence of any kind of values

def odds(start: int , stop: int):
    """Generator inclusive sequence"""
    for odd in range(start, stop + 1, 2):
        #yiels: return out value and then pause
        # with next(), ask the function to resume
        yield odd


# Corouritines: (Consumer) Consume values

# In order to use await, we need the function to be async
async def randn():
    #await allows this particular function to pause
    # But other things can continue to run. 
    # We could imagine this as "running in the background"
    await asyncio.sleep(3)
    return randint(1,10)

def main():
    odd_values = [odd for odd in odds(3,15)]
    print(odd_values)
    odds2 = tuple(odds(21,29))
    print(odds2)


if __name__ == "__main__":
    main()
