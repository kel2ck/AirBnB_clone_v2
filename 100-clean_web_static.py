#!/usr/bin/python3
# Fabric file to delete out-of-date archives.

import os
from operator import length_hint
from fabric.api import run, local, cd, env

env.hosts = ["52.207.208.87", "54.166.141.169"]

def do_clean(number=0):
    """Cleans all .tgz files"""

    number = int(number)
    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
