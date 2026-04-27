'''
Copyright 2015-2022 HENNGE K.K. (formerly known as HDE, Inc.)
Licensed under MIT.
'''
import json
import os
def export_variables(environment_variables):
    pass
def set_environment_variables(json_file_path):
    """
    Read and set environment variables from a flat json file.
    Bear in mind that env vars set this way and later on read using
    `os.getenv` function will be strings since after all env vars are just
    that - plain strings.
    Json file example:
    ```
    {
        "FOO": "bar",
        "BAZ": true
    }
    ```
    :param json_file_path: path to flat json file
    :type json_file_path: str
    """
    pass
