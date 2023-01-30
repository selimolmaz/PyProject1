import requests
import asyncio

from modules.AsyncModule import run_async

@run_async
async def get(url):
    response = await asyncio.ensure_future(requests.get(url))
    httpCode = response.status_code # HTTP cevabının durum kodunu yazdırır
    json = response.json() # Cevabın JSON verisini yazdırır
    return (httpCode, json)