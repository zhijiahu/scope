
import aiohttp
import asyncio
import async_timeout
import argparse
import yaml
import os
import glob
from urllib.parse import urljoin
from datetime import datetime

from elasticsearch_async import AsyncElasticsearch
from elasticsearch.connection.http_urllib3 import create_ssl_context
import certifi


ap = argparse.ArgumentParser()
ap.add_argument('-s', '--scenarios-dir',
                default='scenarios',
                help='Directory to your scenarios. Defaults to current directory')

args = vars(ap.parse_args())


async def request(session, url):
    print('[INFO] [{}] IN PROGRESS...'.format(url))
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.text()

async def main():
    context = create_ssl_context(cafile=certifi.where())
    es = AsyncElasticsearch(
        hosts=['192.168.99.100'],
        ssl_context=context,
        http_auth=('kibana', 'changeme'))

    scenario_files = glob.glob('{0}/*.yml'.format(args['scenarios_dir']))

    for path in scenario_files:
        with open(path, 'r') as config_file:
            config = yaml.load(config_file)

        for scenario in config['scenarios']:
            async with aiohttp.ClientSession() as session:
                base_url = config['backends'][scenario['backend']]
                url = urljoin(base_url, scenario['url'])
                result = await request(session, url)

                print('[INFO] [{}] COMPLETED: {}'.format(url, result))

            doc = {'url': url, 'result': 'Pass', 'timestamp': datetime.now()}
            res = await es.index(index="test-index", doc_type=scenario['backend'], id=1, body=doc)
            print(res['created'])

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
