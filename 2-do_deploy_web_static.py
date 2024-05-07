#!/usr/bin/python3
"""
Using Fabric to distribute an archive to my web servers,
using the function `do_deploy`
"""

from fabric.state import env
from fabric.api import local, put, run
import os
import importlib
module_name = "1-pack_web_static"
module = importlib.import_module(module_name)

env.hosts = ['34.207.64.86', '54.158.217.146']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'

do_pack()


def do_deploy(archive_path):
    """
        Distributes an archive to my web servers
    """
    for host in env.hosts:
        if not os.path.exists(archive_path):
            return False
        filename = archive_path.replace("versions/",
                                        "").replace(".tgz", "").strip()
        base_path = '/data/web_static/'
        if put(archive_path, '/tmp/').failed:
            return False
        if run('mkdir -p {0}releases/{1}/'.format(base_path,
                                                  filename)).failed:
            return False
        if run('tar -xzf /tmp/{2}.tgz -C {0}releases/{2}/'
               ''.format(base_path,
                         archive_path,
                         filename)).failed:
            return False
        if run('rm /tmp/{}.tgz'.format(filename)).failed:
            return False
        if run('cp -r {0}releases/{1}/web_static/* '
               '{0}releases/{1}/'.format(base_path,
                                         filename)).failed:
            return False
        if run('rm -rf {0}releases/{1}/web_static'.format(base_path,
                                                          filename)).failed:
            return False
        if run('rm -rf /data/web_static/current').failed:
            return False
        if run('ln -s {0}releases/{1} {0}current'.format(base_path,
                                                         filename)).failed:
            return False
        print("New version deployed")
    return True
