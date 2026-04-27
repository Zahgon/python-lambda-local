'''
Copyright 2015-2022 HENNGE K.K. (formerly known as HDE, Inc.)
Licensed under MIT.
'''

import signal
import threading
from contextlib import contextmanager
import _thread


class TimeoutException(Exception):
    pass


@contextmanager
def time_limit(seconds):
    pass
