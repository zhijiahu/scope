
import aiohttp
import asyncio
import async_timeout
import argparse
import yaml
import os
from urllib.parse import urljoin


ap = argparse.ArgumentParser()
args = vars(ap.parse_args())


async def request(session, url):
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.text()

async def main():

    path = os.path.join(os.path.dirname(__file__), '../examples/check_google.yml')

    with open(path, 'r') as config_file:
        config = yaml.load(config_file)

    for scenario in config['scenarios']:
        async with aiohttp.ClientSession() as session:
            base_url = config['backends'][scenario['backend']]
            result = await request(session, urljoin(base_url, scenario['url']))
            print(result)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
