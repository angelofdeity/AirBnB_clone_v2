#!/usr/bin/python3
"""This script distributes an archive to web servers, using the function
do_deploy"""
import os
from fabric.api import run, env, cd, put
env.hosts = ['54.208.84.31', '54.172.141.180']
env.user = "ubuntu"


def do_deploy(archive_path):
    """This function distributes an archive to web servers"""
    if (os.path.exists(archive_path) is False):
        return False
    filename = f'/data/web_static/releases/{archive_path.strip(".tgz")}'
    archive = archive_path.lstrip('versions/')
    run(f'mkdir -p {filename}')
    # run('mkdir /tmp/versions')
    put(f'{archive_path}', "/tmp/")
    run(f'tar -xzf /tmp/{archive} -C {filename}')
    run(f'mv {filename}/web_static/* {filename}')
    run(f'rm -rf {filename}/web_static/')
    run(f'rm /tmp/{archive}')
    run('rm /data/web_static/current')
    run(f'ln -sf {filename} /data/web_static/current')
    return True
