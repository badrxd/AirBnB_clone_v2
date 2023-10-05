#!/usr/bin/python3
""" Write a Fabric script that generates a .tgz archive
from the contents of the web_static folder of your AirBnB
Clone repo, using the function do_pack.
"""
import time
from os import path
from fabric.api import local


def do_pack():
    """create tgz"""

    try:
        if path.isdir("versions") is False:
            local("mkdir-p versions")
        date = time.strftime('%Y%m%d%H%M%S')
        fileName = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(fileName))
        return fileName
    except Exception:
        return None
