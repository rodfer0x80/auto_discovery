#!/usr/bin/python3


# Send GET and POST request trying HTTPS and HTTP 
# Read robots.txt
# Parse and sort data to enumerate sitemap
# Return string of sitemap entries newline separated


import sys, requests


def get_robot_txt(host):
    output = ""

    try:
        res = requests.get(f"http://{host}/robots.txt")
        print(res.status_code) 
        if res.status_code != 200:
            res = requests.get(f"https://{host}/robots.txt")
            if res.status_code != 200:
                output = res.text
            else:
                sys.stderr.write("[get_robot_txt] Failed to connect to server\n")
                exit(0)
        else:
            output = res.text
        
    except:
        sys.stderr.write("[get_robot_txt] Network connection error\n")
        exit(1)
   
    return output


if __name__ == '__main__':
    host = False
    try:
        host = sys.argv[1]
    except:
        sys.stderr.write("Usage: ./get_robot_txt.py <host>\n")
        exit(1)
    output = get_robot_txt(host)
    print(output)
    exit(0)
