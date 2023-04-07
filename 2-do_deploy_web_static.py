#!/usr/bin/python3
"""A fab file to archive a folder"""
from datetime import datetime
from fabric.api import local, run, put, env
from fabric.decorators import runs_once
import os


env.hosts = ['34.202.159.232', '100.24.236.27']
def do_deploy(archive_path):
    """Distribute an archive to the remote hosts"""
    # Returns False if the file at the path archive_path doesn’t exist
    if not os.path.exists(archive_path):
        return False
    try:
        # The script should take the following steps:
        full_name = archive_path.rsplit("/", 1)[-1]
        no_extension = full_name.rsplit(".", 1)[0]
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")
        # Uncompress the archive
        run("mkdir -p /data/web_static/releases/{}".format(no_extension))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(full_name, no_extension))
        # Delete the archive from the web server
        run("rm /tmp/{}".format(full_name))
        # Delete the symbolic link /data/web_static/current
        run("rm /data/web_static/current")
        # Create a new symbolic link
        run("ln -s /data/web_static/releases/{} /data/web_static/current".format(no_extension))
        return True
    except Exception:
        return False
