#!/usr/bin/python3
"""
generates a `.tgz` archive from the contents of the `web_static` folder.
"""

from fabric.api import local

def do_pack():
    """"
    generates a `.tgz` archive
    """
    local('mkdir -p versions')
    date = local('date +"%Y%m%d%H%M%S"', capture=True)
    folder = "/root/AirBnB_clone_v2/web_static"
    archive = "versions/web_static_{}.tgz".format(date)
    result = local("tar -cvzf {} web_static".format(archive))

    if result.succeeded:
        return archive
    return None
