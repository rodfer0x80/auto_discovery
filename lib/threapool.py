from .get_robots_txt import get_robots_txt
from .get_sitemap_xml import get_sitemap_xml
from .get_server_id import get_server_id
from .get_favicon_framework import get_favicon_framework
import threading


# sync threads to write to tmpfile in order
flag = 0


def kill_threads():
    global flag
    flag = 0


def run_threads():
    tmpfile = "/tmp/auto_discovery.tmp"
    global flag
   
    if os.exists(tmpfile):
        os.umask(660)
        os.remove(tmpfile)
    
    # to thread things

    with open(tmpfile, 'r') as fp:
        data = fp.read().splitlines()
        for line in data:
            print(line)
    os.remove(tmpfile)
    exit(0)
