#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers, using the function do_deploy
"""

from fabric.api import run, put, env
from os.path import exists
env.hosts = ['drkhali.tech', '100.25.38.121']


def do_deploy(archive_path):
    """Deploy archive for the web content in web_static"""
    if exists(archive_path) is False:
        return False
    try:
        path = archive_path.split('/')[-1]
        no_ext_path = path.replace('.tgz', '')
        release_path = '/data/web_static/releases/'
        symlink_curr = '/data/web_static/current'
        put(archive_path, '/tmp/')
        run('mkdir -p {}/{}'.format(release_path, no_ext_path))
        run('tar -xzf /tmp/{} -C {}/{}'.format(
            path, release_path, no_ext_path))

        run('rm -rf /tmp/{}'.format(path))
        run('mv {0}{1}/web_static/* {0}/{1}'.format(
            release_path, no_ext_path))
        run('rm -rf {}/{}/web_static {} '.format(
            release_path, no_ext_path))
        run('ln -s {} {}/{}'.format(
            symlink_curr, release_path, no_ext_path))
        return True
    except:
        return False
