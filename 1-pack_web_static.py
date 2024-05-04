#!/usr/bin/python3
'''generates a `.tgz` archive from the contents of the `web_static` folder.'''
from fabric.api import local

def do_pack():
    date = local('date +"%Y%m%d%H%M%S"', capture=True)
    folder = "/root/AirBnB_clone_v2/web_static"
    archive = "web_static_{}.tgz".format(date)
    result = local("tar -cvzf {} {}".format(archive, folder), capture=True)

    if result.succeeded:
        return archive
    return None
