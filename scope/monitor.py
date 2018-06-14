
import aiohttp
import asyncio
import async_timeout
import yaml
import os
import glob
from urllib.parse import urljoin
from collections import defaultdict
import time

from scope.tracker.trackerfactory import TrackerFactory


class Monitor(object):

    def __init__(self, scenarios_dir, duration=None, tracker_type=None, tracker_url_token=None):
        self.scenarios_dir = scenarios_dir
        self.duration = duration
        self.tracker_type = tracker_type
        self.tracker_url_token = tracker_url_token

    async def start(self):
        tracker = TrackerFactory.create_tracker(self.tracker_type, self.tracker_url_token)
        counter = defaultdict(int)
        scenario_files = glob.glob('{0}/*.yml'.format(self.scenarios_dir))

        start = int(time.time())
        while True:
            now = int(time.time())
            if self.duration is not None and (now - start) > int(self.duration):
                return

            for path in scenario_files:
                with open(path, 'r') as config_file:
                    config = yaml.load(config_file)

                for scenario in config['scenarios']:
                    try:
                        async with aiohttp.ClientSession() as session:
                            base_url = config['backends'][scenario['backend']]
                            url = urljoin(base_url, scenario['url'])

                            counter[url] += 1

                            result = await self.__request(session, url)

                            print('DONE')
                            tracker.report_stats(dict(counter))

                    except:
                        tracker.report_error()

            await asyncio.sleep(1)

    async def __request(self, session, url):
        print('[INFO] [{}] ... '.format(url), end='', flush=True)

        with async_timeout.timeout(10):
            async with session.get(url) as response:
                return await response.text()
