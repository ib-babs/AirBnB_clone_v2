#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers, using the function do_deploy
"""

from fabric.api import run, put, env
from datetime import datetime
from os.path import exists
env.hosts = ['drkhali.tech', '100.25.38.121']


def do_deploy(archive_path):
    """Deploy archive for the web content in web_static"""
    if exists(archive_path) is False:
        return False
    try:
        tmp_archive = '/tmp/{}'.format(archive_path)
        tmp_archive_no_ext = '/tmp/{}'.format(archive_path.replace(".tgz", ''))
        symlink_curr = "/data/web_static/current"
        release_data = "/data/web_static/releases/".format(
            tmp_archive_no_ext
        )
        put(archive_path, '/tmp/')
        run('tar -xzf {} -C {}'.format(
            tmp_archive, release_data))
        run('rm -rf {} /data/web_static/current'.format(tmp_archive_no_ext))
        run('ln -s {} /data/web_static/releases/{}'.format(
            symlink_curr, tmp_archive_no_ext))
        return True
    except:
        return False
