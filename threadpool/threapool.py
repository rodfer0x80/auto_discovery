import threading


from lib.get_robots_txt import get_robots_txt
from lib.get_sitemap_xml import get_sitemap_xml
from lib.get_server_id import get_server_id
from lib.get_favicon_framework import get_favicon_framework


class Threadpool:
    def __init__(self):
        self.mutex_setup()

    def start_timer(self):
        self.start = time.time()


    def get_time_elapsed(self):
        if self.start:
            finish = time.time()
            time_elapsed = finish - start
            del self.start
            del self.finish
            return "%.2f seconds" % time_elapsed
        else:
            sys.stderr.write("[get_time_elapsed] Timer was not started\n")
            return "n/a"


    def mutex_setup(self):
        self.mutex_lock = False
        self.mutex = "/tmp/auto_discovery.tmp"
        os.umask(660)
        if os.exists(self.mutex):
            os.remove(self.mutex)
        os.system(f"touch {self.mutex}")


    def mutex_cleanup(self):
        os.umask(660)
        os.system("mv {self.mutex} report.log")
        os.remove(self.mutex)


    def mutex_write(self, data):
        while self.mutex_lock:
            sleep(1)
        try:
            with open(self.mutex, 'a') as fp:
                fp.write(data)
        except FileNotFound:
            self.mutex_setup()
            self.mutex_write(data)


    def create_threads(self):
        # create n number of threads with a list of function calls
        # and run then in parallel
        return None


