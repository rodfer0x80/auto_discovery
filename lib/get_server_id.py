#!/usr/bin/python3


# Send GET and POST request trying HTTPS and HTTP 
# Read Server header from response
# Return Server ID string


import sys, requests


def get_server_id(host):
    output = ""
    
    try:
        res = requests.get(f"http://{host}/")
        output = res.headers['Server']
        if output != "" and output != None:
            res = requests.post(f"http://{host}/")
            output = res.headers['Server']
        
        if output != "" and output != None:
            res = requests.get(f"https://{host}/")
            output = res.headers['server']
        
        if output != "" and output != None:
            res = requests.post(f"https://{host}/")
            output = res.headers['server']

        
        if output != "" and output != None:
            sys.stderr.write("[get_server_id] Failed to connect to server\n")
            exit(0)
    except:
        print("[get_server_id] Network connection error\n")
        exit(1)
    
    return output

