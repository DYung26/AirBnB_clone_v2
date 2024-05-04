#!/usr/bin/python3
"""
Using Fabric to distribut an archive to my web servers,
using the function `do_deploy`
"""
from fabric.state import env
from fabric.api import local, put, run
import os

env.hosts = ['34.207.64.86', '54.158.217.146']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa.pub'


def do_deploy(archive_path):
    """
        Distributes an archive to my web servers
    """
    try:
        for host in env.hosts:
            if not os.path.exists(archive_path):
                return False
            filename = archive_path.replace("versions/",
                                            "").replace(".tgz", "").strip()
            base_path = '/data/web_static/'
            put(archive_path, '/tmp/')
            run('mkdir  -p {0}releases/{1}'.format(base_path, filename))
            run('tar -xzf {1} -C {0}releases/{2}'.format(base_path,
                                                           archive_path,
                                                           filename))
            run('rm /tmp/{}'.format(archive_path))
            run('mv {0}releases/{1}/web_static/* '
                  '{0}releases/{1}/'.format(base_path,
                                            filename))
            run('rm -rf {0}releases/{1}/web_static/'.format(base_path,
                                                              filename))
            run('rm -rf /data/web_static/current')
            run('ln -s {0}releases/{1} {0}current'.format(base_path,
                                                            filename))
            print("New version deployed")
        return True
    except Exception as e:
        return False
