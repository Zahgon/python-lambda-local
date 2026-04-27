'''
Copyright 2015-2022 HENNGE K.K. (formerly known as HDE, Inc.)
Licensed under MIT.
'''
import sys
import traceback
import json
import logging
import os
import timeit
import multiprocessing
from . import event
from . import context
from .environment_variables import set_environment_variables, export_variables
from .timeout import time_limit
from .timeout import TimeoutException
logging.basicConfig(stream=sys.stdout,
                    level=logging.INFO,
                    format='[%(name)s - %(levelname)s - %(asctime)s] %(message)s')
ERR_TYPE_EXCEPTION = 0
ERR_TYPE_TIMEOUT = 1
EXITCODE_ERR = 1
class ContextFilter(logging.Filter):
    def __init__(self, context):
        super(ContextFilter, self).__init__()
        self.context = context
    def filter(self, record):
        pass
class FunctionLoader():
    def __init__(self,
                 request_id=None,
                 source=None,
                 function_name=None,
                 library_path=None,
                 func=None):
        self.request_id = request_id
        self.source = source
        self.function_name = function_name
        self.library_path = library_path
        self.func = func
    def load(self):
        pass
def call(func, event, context, environment_variables={}):
    pass
def run(args):
    pass
def _runner(loader, event, context):
    pass
def load_lib(path):
    pass
def load_source(request_id, path, function_name):
    pass
def execute(func, event, context):
    pass
def execute_in_process(queue, loader, event, context):
    pass
