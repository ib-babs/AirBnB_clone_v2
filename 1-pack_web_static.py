#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo, using the function do_pack.
"""

from fabric.api import local
import datetime
from os.path import isdir


def do_pack():
    """Create archive for the web content in web_static"""
    try:
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir('versions') is False:
            local('mkdir versions')
        archive_path = "versions/web_static_{}.tgz".format(now)
        local('tar -czvf {} web_static'.format(archive_path))
        return archive_path
    except Exception as e:
        return None
