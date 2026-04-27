'''
Copyright 2015-2022 HENNGE K.K. (formerly known as HDE, Inc.)
Licensed under MIT.
'''
from __future__ import print_function

from datetime import datetime
from datetime import timedelta
import uuid


class Context(object):
    def __init__(self, timeout_in_seconds,
                 aws_request_id=uuid.uuid4(),
                 function_name="undefined",
                 function_version="$LATEST",
                 log_group_name="undefined",
                 log_stream_name="undefined",
                 invoked_function_arn="undefined",
                 memory_limit_in_mb='0',
                 client_context=None,
                 identity=None):
        self.function_name = function_name
        self.function_version = function_version
        self.invoked_function_arn = invoked_function_arn
        self.memory_limit_in_mb = memory_limit_in_mb
        self.aws_request_id = aws_request_id
        self.log_group_name = log_group_name
        self.log_stream_name = log_stream_name
        self.identity = identity
        self.client_context = client_context

        self._timeout_in_seconds = timeout_in_seconds
        self._duration = timedelta(seconds=timeout_in_seconds)

    def get_remaining_time_in_millis(self):
        pass

    def log(self, msg):
        pass

    def _activate(self):
        pass


def millis_interval(start, end):
    """start and end are datetime instances"""
    pass
