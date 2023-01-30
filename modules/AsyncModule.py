import asyncio

def run_async(func):
    async def wrapper(*args, **kwargs):
        return await asyncio.gather(func(*args, **kwargs))
    return wrapper


