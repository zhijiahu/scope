
from abc import ABC, abstractmethod


class Tracker(ABC):

    @abstractmethod
    def report_error(self, error_message):
        pass

    @abstractmethod
    def report_stats(self, stats):
        pass


class NullTracker(Tracker):

    def report_error(self, error_message=''):
        pass

    def report_stats(self, stats):
        pass
