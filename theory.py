# Generators : sequence of any kind of values

def odds(start: int , stop: int):
    """Generator inclusive sequence"""
    for odd in range(start, stop + 1, 2):
        #yiels: return out value and then pause
        # with next(), ask the function to resume
        yield odd
