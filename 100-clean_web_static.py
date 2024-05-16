#!/usr/bin/python3
"""Fabric script (based on the file 3-deploy_web_static.py)
that deletes out-of-date archives"""

import os
from fabric.api import *

env.hosts = ["54.209.208.34", "100.26.223.59"]


def do_clean(number=0):
    """Settuping the Function"""
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
