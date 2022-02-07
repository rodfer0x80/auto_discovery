#!/usr/bin/python3


# Send GET request trying HTTPS and HTTP 
# Read header from response to get favicon.ico
# md5sum and compare with database for match


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


if __name__ == '__main__':
    owasp_favicon_db = "./owasp_favicon_db.txt"
    arg1_model = "<IPv4>"
    if len(sys.argv) != 2:
        sys.stderr.write(f"Usage: ./{sys.argv[0]} {arg1_model}\n")
        exit(1)
    host = sys.argv[1]
    try:
        db = unpack_txt_db(owasp_favicon_db)
    except FileNotFound:
        print("[!] File not found at {owasp_favicon_db}")
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
            print("[!] Failed to connect to server\n")
            exit(1)
    except:
        print("[!] Network connection error")
        exit(1)

    hash_ob = hashlib.md5(output.strip().encode())
    hashed_pass = hash_ob.hexdigest()
    print(hashed_pass)
    for fw_hash in db:
        if fw_hash == hashed_pass:
            print(db[fw_hash])
            break
    exit(0)

