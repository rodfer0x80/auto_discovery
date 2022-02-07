#!/usr/bin/python3


# Send GET and POST request trying HTTPS and HTTP 
# Read Server header from response
# Return Server ID data


import sys, requests


if __name__ == '__main__':
    arg1_model = "<IPv4>"
    if len(sys.argv) != 2:
        sys.stderr.write(f"Usage: ./{sys.argv[0]} {arg1_model}\n")
        exit(1)
    host = sys.argv[1]

    try:
        # GET HTTP
        res = requests.get(f"http://{host}/sitemap.xml")
        output = res.text
    except:
        try:
            # GET HTTPS
            res = requests.get(f"https://{host}/")
            output = res.headers['server']
        except:
            output = "[!] Failed to connect to server\n"
    print(output)

