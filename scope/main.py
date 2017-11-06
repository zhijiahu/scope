
import aiohttp
import asyncio
import async_timeout
import argparse
import yaml
import os
import glob
from urllib.parse import urljoin


ap = argparse.ArgumentParser()
ap.add_argument('-s', '--scenarios-dir',
                default='scenarios',
                help='Directory to your scenarios. Defaults to current directory')

args = vars(ap.parse_args())


async def request(session, url):
    print('[INFO] Checking {}'.format(url))
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.text()

async def main():

    scenario_files = glob.glob('{0}/*.yml'.format(args['scenarios_dir']))

    for path in scenario_files:
        with open(path, 'r') as config_file:
            config = yaml.load(config_file)

        for scenario in config['scenarios']:
            async with aiohttp.ClientSession() as session:
                base_url = config['backends'][scenario['backend']]
                result = await request(session, urljoin(base_url, scenario['url']))
                print(result)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
