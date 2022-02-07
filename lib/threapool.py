import threading

from .get_robots_txt import get_robots_txt
from .get_sitemap_xml import get_sitemap_xml
from .get_server_id import get_server_id
from .get_favicon_framework import get_favicon_framework


# sync threads to write to tmpfile in order
flag = 0


def kill_threads():
    global flag
    flag = 0


def run_threads():
    global flag
    tmpfile = "/tmp/auto_discovery.tmp"
    os.umask(660)

    if os.exists(tmpfile):
        os.remove(tmpfile)
    os.system(f"touch {tmpfile}")
    
    # to thread things

    os.remove(tmpfile)
    exit(0)
