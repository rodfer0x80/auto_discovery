#!/usr/bin/python3


# Send GET and POST request trying HTTPS and HTTP 
# Read Server header from response
# Return Server ID data


import sys, requests


if __name__ == '__main__':
    arg1_model = "<IPv4>"
    if len(sys.argv) != 2:
        sys.stderr.write(f"Usage: ./{sys.argv[0]} {arg1_model}\n")
        print(1)
        exit(1)
    host = sys.argv[1]
    
    
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
            sys.stderr.write("[!] Failed to connect to server\n")
            print(1)
            exit(0)
    except:
        print("[!] Network connection error\n")
        print(1)
        exit(1)

    print(output)

