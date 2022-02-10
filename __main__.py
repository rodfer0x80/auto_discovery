#\!/usr/bin/python3


from lib.threading import run_threads


def bootstrap():
    if len(os.argv) != 2:
        sys.stderr.write("Usage:/ python3 __main__.py <host>\n")
        exit(1)
    host = os.argv[1]
    threadpool = Threadpool(host)
    threadpool.start_timer()
    threadpool.run_threads()
    if threadpool.run_threads() == 0:
        time_elapsed = threadpool.get_time_elapsed()
        print(f"[*] Report build in {time_elapsed} and saved to ./report ")
    exit(0)


if __name__ == '__main__':
    bootstrap()


