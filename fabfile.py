#!/usr/bin/python3
from datetime import datetime
from fabric.api import local
"""This script"""
def do_pack():
    archive = f"web_static_{datetime.now().strftime('%Y%m%d%H%M%S')}"
    local("mkdir ~/versions")
    local(f'tar czf {archive}.tgz /versions')
