#!/usr/bin/python3
"""
Creates and distributes an archive to your web servers,
using the function `deploy`.
"""
from fabric.state import env
from fabric.api import local, run
import importlib
module_name = "1-pack_web_static"
module = importlib.import_module(module_name)
module_name1 = "2-do_deploy_web_static"
module1 = importlib.import_module(module_name1)


def deploy():
    """
        Creates and distributes an archive to my web servers.
    """
    path = module.do_pack()
    if path is False:
        return False
    ret_val = module1.do_deploy(path)
    return ret_val
