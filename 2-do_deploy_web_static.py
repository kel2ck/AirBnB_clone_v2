#!/usr/bin/python3
"""A fabric script that distributes an archive to web servers"""
from datetime import datetime
from fabric.api import local, run, put, env
from fabric.decorators import runs_once
import os


env.hosts = ['52.207.208.87', '54.166.141.169']


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
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}"
            .format(full_name, no_extension))
        # Delete the archive from the web server
        run("rm -rf /tmp/{}".format(full_name))
        # Delete the symbolic link /data/web_static/current
        run("rm -rf /data/web_static/current")
        # Create a new symbolic link
        run("ln -s /data/web_static/releases/{}/web_static \
                /data/web_static/current".format(no_extension))
        return True
    except Exception:
        return False
