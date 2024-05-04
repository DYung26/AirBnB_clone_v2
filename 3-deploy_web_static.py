#!/usr/bin/python3
"""
Creates and distributes an archive to your web servers,
using the function `deploy`.
"""
from fabric import env
from fabric.api import local, run
from 1-pack_web_static import do_pack
from 2-do_deploy_web_static import do_deploy

def deploy():
    """
        Creates and distributes an archive to my web servers.
    """
    path = do_pack()
    if path is False:
        return False
    ret_val = do_deploy(path)
    return ret_val
