from config import api_url
import aiohttp, asyncio
import pprint

async def fetch(session, url):
    async with session.get(api_url + url) as response:
        return await response.json()

async def get_autos():
    async with aiohttp.ClientSession() as session:
        data = await fetch(session, "api/autolar/")
        return data

async def get_orders():
    async with aiohttp.ClientSession() as session:
        data = await fetch(session, "api/orders/")
        return data

async def get_order(id):
    id = str(id)
    async with aiohttp.ClientSession() as session:
        data = await fetch(session, "api/orders/" + id)
        return data

async def get_customer(id):
    id = str(id)
    async with aiohttp.ClientSession() as session:
        data = await fetch(session, "api/customers/" + id)
        return data

async def get_recent_orders():
    async with aiohttp.ClientSession() as session:
        data = await fetch(session, "api/recent-orders/")
        return data


