import aiohttp
import asyncio
import os
from dotenv import load_dotenv
load_dotenv()

async def fetch_data_1(url):
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        async with session.get(url) as response:
            await asyncio.sleep(3)
            data = await response.json()
            print(data)

async def fetch_data_2(url):
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        async with session.get(url) as response:
            await asyncio.sleep(2)
            data = await response.json()
            print(data)

async def fetch_data_3(url):
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        async with session.get(url) as response:
            await asyncio.sleep(1)
            data = await response.json()
            print(data)

async def main():
    # auth_url = f"https://v6.exchangerate-api.com/v6/{os.getenv("API_KEY")}/latest/USD"
    url_1 = f"https://v6.exchangerate-api.com/v6/{os.getenv("API_KEY")}/latest/USD"
    url_2 = f"https://v6.exchangerate-api.com/v6/{os.getenv("API_KEY")}/latest/EGP"
    url_3 = f"https://v6.exchangerate-api.com/v6/{os.getenv("API_KEY")}/latest/EUR"
    await asyncio.gather(
        asyncio.create_task(fetch_data_1(url_1)),
        asyncio.create_task(fetch_data_1(url_2)),
        asyncio.create_task(fetch_data_1(url_3))
    )

asyncio.run(main())
