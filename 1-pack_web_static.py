#!/usr/bin/python3
"""This module contains a script that generates a .tgz archive from the
contents of the web_static folder of your AirBnB Clone repo, using the
function do_pack.
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """This function generates a .tgz archive from the contents of the
    web_static folder of your AirBnB Clone repo, using the function do_pack.
    """
    if not os.path.exists("versions"):
        if local("mkdir versions").failed:
            return None
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file = f"versions/web_static_{date}.tgz"
    if local(f"tar -cvzf {file} ./web_static").failed:
        return None
    return file
