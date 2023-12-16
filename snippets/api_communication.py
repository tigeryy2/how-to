"""
API Communication Snippet

Description:
    This snippet is used when you need to communicate with an API. While the most popular library for this is `requests`,
    I choose to use `httpx` because it is a newer library that is more modern and has async support.

    This example is borrowed from https://github.com/ArjanCodes/examples/blob/main/2023/httpx/httpx_example_async.py

    It uses `asyncio` to make the requests asynchronously, which is much faster than making the requests synchronously.

Dependencies:
    httpx

References:
    https://www.youtube.com/watch?v=OPyoXx0yA0I
    https://github.com/ArjanCodes/examples/tree/main/2023/httpx
"""

import asyncio
import time
from typing import Any

import httpx

BASE_URL = "https://httpbin.org"


async def fetch_get(client: httpx.AsyncClient) -> Any:
    response = await client.get(f"{BASE_URL}/get")
    return response.json()


async def fetch_post(client: httpx.AsyncClient):
    data_to_post = {"key": "value"}
    response = await client.post(f"{BASE_URL}/post", json=data_to_post)
    return response.json()


async def fetch_put(client: httpx.AsyncClient):
    data_to_put = {"key": "updated_value"}
    response = await client.put(f"{BASE_URL}/put", json=data_to_put)
    return response.json()


async def fetch_delete(client: httpx.AsyncClient):
    response = await client.delete(f"{BASE_URL}/delete")
    return response.json()


async def main():
    # record the starting time
    start = time.perf_counter()

    async with httpx.AsyncClient() as client:
        tasks = [
            fetch_get(client),
            fetch_post(client),
            fetch_put(client),
            fetch_delete(client),
        ]
        results = await asyncio.gather(*tasks)

    for result in results:
        print(result)

    # record the ending time
    end = time.perf_counter()
    print(f"Time taken: {end - start:.2f} seconds.")


# To run the function
if __name__ == "__main__":
    asyncio.run(main())
