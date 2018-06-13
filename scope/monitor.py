
import aiohttp
import asyncio
import async_timeout
import argparse
import yaml
import os
import glob
from urllib.parse import urljoin
from collections import defaultdict

from tracker.trackerfactory import TrackerFactory


ap = argparse.ArgumentParser()
ap.add_argument('-s', '--scenarios-dir',
                default='scenarios',
                help='Directory to your scenarios. Defaults to current directory')

ap.add_argument('-t', '--tracker',
                default=None,
                help='Type of tracker that records the monitoring. No tracker by default, just check the console output')

ap.add_argument('-u', '--trackerurlortoken',
                default=None,
                help='Url or token for the tracker')

args = vars(ap.parse_args())

async def request(session, url):
    print('[INFO] [{}] ... '.format(url), end='', flush=True)

    with async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.text()

async def main():

    tracker = TrackerFactory.create_tracker(args['tracker'], args['trackerurlortoken'])

    counter = defaultdict(int)
    scenario_files = glob.glob('{0}/*.yml'.format(args['scenarios_dir']))

    while True:
        for path in scenario_files:
            with open(path, 'r') as config_file:
                config = yaml.load(config_file)

            for scenario in config['scenarios']:
                try:
                    async with aiohttp.ClientSession() as session:
                        base_url = config['backends'][scenario['backend']]
                        url = urljoin(base_url, scenario['url'])

                        counter[url] += 1
                        result = await request(session, url)

                        print('DONE')
                        tracker.report_stats(dict(counter))

                except:
                    tracker.report_error()

        await asyncio.sleep(1)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
