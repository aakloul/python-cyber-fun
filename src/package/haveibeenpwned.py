#!/usr/bin/env python

import requests
import sys
import json
import hashlib

headers = {"hibp-api-key": ""}
headers = None


def check_password(password):
    m = hashlib.sha1()
    m.update(password.encode())
    return check_password_hash(m.hexdigest())


def check_password_hash(password_hash):
    try:
        password_hash = password_hash.upper()
        url = f"https://api.pwnedpasswords.com/range/{password_hash[0:5]}"
        r = requests.get(url, verify=True)
        if r.status_code == 404:
            x = f"Password: {password_hash} has not been pwned"
            return x
        if r.status_code == 200:
            for line in r.text.split("\n"):
                if password_hash[5:] in line:
                    times = line.strip().split(":")[1]
                    x = f"Password {password_hash} has been pwned {times} times"
                    return x
            x = f"Password: {password_hash} has not been pwned"
            return x
        else:
            return r.json()
            # pass
    except Exception as e:
        return str(e)


def check_email(email):
    try:
        url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
        r = requests.get(url, headers=headers, verify=True)
        if r.status_code == 404:
            x = f"Account: {email} has not been pwned"
            return x
        if r.status_code == 200:
            j = r.json()
            x = json.dumps(
                j,
                indent=2,
                separators=(",", ": "),
                ensure_ascii=False,
                encoding="utf-8",
            )
            return x
        else:
            return r.json()
            # pass
    except Exception as e:
        return str(e)


def check_pastebin(email):
    try:
        url = f"https://haveibeenpwned.com/api/v3/pasteaccount/{email}"
        r = requests.get(url, headers=headers, verify=True)
        if r.status_code == 404:
            x = "Account: {email} has not been pasted"
            return x
        if r.status_code == 200:
            j = r.json()
            x = json.dumps(
                j,
                indent=2,
                separators=(",", ": "),
                ensure_ascii=False,
                encoding="utf-8",
            )
            return x
        else:
            return r.json()
            # pass
    except Exception as e:
        return str(e)


email = sys.argv[1]
password = sys.argv[1]
# password = "password"
p = check_password(password)
print(p)
exit()
t = check_email(email)
print(t)
q = check_pastebin(email)
print(q)
