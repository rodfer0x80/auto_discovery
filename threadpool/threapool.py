import threading, os, sys, time


#from get_robots_txt import get_robots_txt
#from get_sitemap_xml import get_sitemap_xml
#from get_server_id import get_server_id
#from get_favicon_framework import get_favicon_framework


class Threadpool:
    def __init__(self):
        self.mutex_setup()

    def start_timer(self):
        self.start = time.time()


    def get_time_elapsed(self):
        if self.start:
            finish = time.time()
            time_elapsed = finish - self.start
            del self.start
            return "%.2f seconds" % time_elapsed
        else:
            sys.stderr.write("[get_time_elapsed] Timer was not started\n")
            return "n/a"


    def mutex_setup(self):
        self.mutex_lock = False
        self.mutex = "/tmp/auto_discovery.tmp"
        os.umask(660)
        if os.path.exists(self.mutex):
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


    def run_threads(self, n_threads=4):
        # create n number of threads with a list of function calls
        # and run then in parallel
        self.threads = list()
        self.n_threads = n_threads
        for i in range(0, n_threads):
            data = "0"
            self.threads.append(threading.Thread(target=self.thread_log_data, args=data))
            self.threads[i].start()
            self.threads[i].join()
        data = ""
        with open(self.mutex, 'r') as fp:
            for line in fp.read().splitlines():
                data += line + "\n"
        return data


    def thread_log_data(self, data):
        self.mutex.write(data)
        return 0
    

if __name__ == '__main__':
    threadpool = Threadpool()
    threadpool.start_timer()
    
    data = threadpool.run_threads()
    time_elapsed = threadpool.get_time_elapsed()
    
    print(data)
    print(time_elapsed)
    
    exit(0)
