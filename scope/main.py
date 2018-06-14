
import asyncio
import argparse

from scope.monitor import Monitor


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

ap.add_argument('-d', '--duration',
                default=None,
                help='Duration of the monitoring in seconds. Defaults to endless monitoring until keyboard interrupt.')

args = vars(ap.parse_args())


async def main():
    monitor = Monitor(args['scenarios_dir'], args['duration'], args['tracker'], args['trackerurlortoken'])
    await monitor.start()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
