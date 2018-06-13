
import rollbar

from .tracker import Tracker


class Rollbar(Tracker):

    def __init__(self, token):
        rollbar.init(token)

    def report_error(self, error_message=''):
        rollbar.report_exc_info()

    def report_stats(self, stats):
        rollbar.report_message(stats, 'info')
