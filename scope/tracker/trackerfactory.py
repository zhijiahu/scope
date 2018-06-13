
from .rollbar import Rollbar


class TrackerFactory():

    @staticmethod
    def create_tracker(tracker_type, tracker_url_token):

        if tracker_type == 'rollbar':
            return Rollbar(tracker_url_token)
