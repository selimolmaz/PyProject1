import asyncio

from modules.GetRequst import get

async def main():
    result = get("http://api.plos.org/search?q=title:DNA")
    print(result)

if __name__ == "__main__":
    asyncio.run(main())