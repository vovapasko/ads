import time
from urllib.request import urlopen
import aiohttp
import asyncio


def get_urls_to_crawl():
    urls_list = list()
    urls_list.append('http://www.cnn.com/')
    urls_list.append('https://www.foxnews.com/')
    urls_list.append('https://www.bbc.com/')
    urls_list.append('https://www.dawn.com')
    urls_list.append('https://www.cnbc.com')
    urls_list.append('https://www.twitter.com')

    return urls_list


def run_sync():
    urls_to_crawl = get_urls_to_crawl()
    start = time.time()

    for url in get_urls_to_crawl():
        html = urlopen(url)
        text = html.read()
        print(url)

    elapsed = time.time() - start
    print("\n{} URLS downloaded in {:.2f}s".format(len(urls_to_crawl), elapsed))


def async_one():
    async def get_data(url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                text = await response.text()
                return text

    async def run_async():
        urls_to_crawl = get_urls_to_crawl()
        start = time.time()

        for url in urls_to_crawl:
            text = await get_data(url)
            print(url)
        elapsed = time.time() - start
        print("\n{} URLS downloaded in {:.2f}s".format(len(urls_to_crawl), elapsed))

    asyncio.run(run_async())


def async_two():
    async def crawl_one_url(url, session):
        get_request = session.get(url)

        res = await get_request
        txt = await res.text()

        get_request.close()

        return txt

    async def crawl_urls(urls_to_crawl):
        session = aiohttp.ClientSession()

        work_to_do = list()
        for url in urls_to_crawl:
            work_to_do.append(crawl_one_url(url, session))

        res = await asyncio.gather(*work_to_do)

        await session.close()
        return res

    t0 = time.time()
    urls_to_crawl = get_urls_to_crawl()
    asyncio.run(crawl_urls(urls_to_crawl))
    elapsed = time.time() - t0
    print("\n{} URLS downloaded in {:.2f}s".format(len(urls_to_crawl), elapsed))


async_one()
async_two()
