import json
import time
import asyncio


import aiohttp

async def worker(name, n, session):
    """make requests on  qrng API . get N random numbers"""
    print(f"worker: {name}")
    url = f"http://qrng.anu.edu.au/API/jsonI.php?length={n}type=uint16"
    # await because we'll do asynchronous io
    response = await session.request(method = 'GET', url = url)
    value = await response.text() 
    if 'limited' in value:
        return value
    else:
        value = json.loads(value)
        return sum(value['data'])
    


async def main():
    async with aiohttp.ClientSession() as session:
        response = await worker('bob', 3, session)
        print("response: ", response)


if __name__ == "__main__": 
    start = time.perf_counter()
    asyncio.run(main( ))
    elapsed = time.perf_counter() - start
    print(f"executed in {elapsed:0.2f} seconds")