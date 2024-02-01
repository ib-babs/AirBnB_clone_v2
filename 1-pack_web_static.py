#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the
contents of the web_static folder of your
AirBnB Clone repo, using the function do_pack."""
from fabric.api import local
import datetime
import os


def do_pack():
    """Create archive for the web content in web_static"""
    if not os.path.exists('versions'):
        os.makedirs('versions')
    try:
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = f"web_static_{now}.tgz"
        archive_path = os.path.join('versions', archive_name)
        local('tar -czvf {} web_static'.format(archive_path))
        return archive_path
    except Exception as e:
        return None
