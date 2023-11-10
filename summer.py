import time
import asyncio


import aiohttp


async def worker(name, n, session):
    """make requests on  qrng API . get N random numbers"""
    print(f"worker: {name}")
    url = f"https://api.quantumnumbers.anu.edu.au"
    params = {'length': n, 'type': 'uint16', 'size': '1'}
    headers = {'x-api-key': 'Z355gDqnFb3NMYytkSGzF4qNNaHtIbTB5raEoo3a'}
    # await because we'll do asynchronous io
    response = await session.get(url, params = params, headers= headers)
    if response.status == 200:
        data = await response.json()
        return sum(data['data'])
    return 0

async def main():
    async with aiohttp.ClientSession() as session:
        sums = await asyncio.gather(*(worker(f'w{i}', n, session) for i, n in enumerate(range(2,5))))
        print("sums: ", sums)


if __name__ == "__main__": 
    start = time.perf_counter()
    asyncio.run(main( ))
    elapsed = time.perf_counter() - start
    print(f"executed in {elapsed:0.2f} seconds")