#!/usr/bin/python3
"""A fab file to archive a folder"""
from datetime import datetime
from fabric.api import local
from fabric.decorators import runs_once


# Prototype: def do_pack():
@runs_once
def do_pack():
    """The funcion to do the archiving"""
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    archive_name = "web_static_" + timestamp + ".tgz"
    local("mkdir -p versions")
    result = local("tar czf versions/{} web_static".format(archive_name))
    if result.failed:
        return None
    return "versions/{}".format(archive_name)
