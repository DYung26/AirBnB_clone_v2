#!/usr/bin/python3
'''generates a `.tgz` archive from the contents of the `web_static` folder.'''
from fabric.api import local

def do_pack():
    local('mkdir -p versions')
    date = local('date +"%Y%m%d%H%M%S"', capture=True)
    folder = "~/AirBnB_clone_v2/web_static"
    archive = "versions/web_static_{}.tgz".format(date)
    #res = local('ls -R web_static', capture=True)
    #lines = res.splitlines()

    #for line in lines:
    #    print(line)
    result = local("tar -cvzf {} {}".format(archive, folder))

    if result.succeeded:
        return archive
    return None
