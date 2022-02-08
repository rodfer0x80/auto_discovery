#!/usr/bin/python3


# Send GET request trying HTTPS and HTTP 
# Read header from response to get favicon.ico
# md5sum and compare with database for match
# Return string "hash\nframework" if framework is found
# Return string "hash" if framework not found


import sys, requests, hashlib


def unpack_txt_db(db_location):
    db = dict()
    
    with open(db_location, 'r') as fp:
        data = fp.read().splitlines()
        for line in data:
            line_sep = line.split(":")
            md5hash, framework = line_sep[0], line_sep[1]
            db[md5hash] = framework
    
    return db


def get_favicon_framework(host, owasp_favicon_db="./owasp_favicon_db.txt"):
    output = ""
    
    try:
        db = unpack_txt_db(owasp_favicon_db)
    except FileNotFound:
        sys.stderr.write("[get_favicon_framework] File not found at {owasp_favicon_db}")
        exit(1)
    
    try:
        res = requests.get(f"http://{host}/favicon.ico")
        res_status_code = res.status_code
        if res_status_code != 200:    
            res = requests.get(f"http://{host}/assets/favicon.ico")
        else:
            output = res.text
    
        if res.status_code != 200:    
            res = requests.get(f"http://{host}/images/favicon.ico")
        else:
            output = res.text
    
        if res.status_code != 200:    
            res = requests.get(f"https://{host}/favicon.ico")
        else:
            output = res.text
    
        if res.status_code != 200:    
            res = requests.get(f"https://{host}/assets/favicon.ico")
        else:
            output = res.text

        if res.status_code != 200:    
            res = requests.get(f"https://{host}/images/favicon.ico")
        else:
            output = res.text
    
        if res.status_code != 200:
            sys.stderr.write("[get_favicon_framework] Failed to connect to server\n")
            exit(0)
    except:
        sys.stderr.write("[get_favicon_framework] Network connection error\n")
        exit(1)

    hash_ob = hashlib.md5(output.strip().encode())
    hashed_pass = hash_ob.hexdigest()
    output = f"{hashed_pass}\n"
    
    for fw_hash in db:
        if fw_hash == hashed_pass:
            output += f"{hashed_pass}:{db[fw_hash]}\n"
            break

    return output

