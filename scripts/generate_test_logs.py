#!/usr/bin/env python3
"""Generateur de journaux de TEST (inoffensif) pour valider les regles Wazuh.

Usage : python3 generate_test_logs.py --scenario ssh_bruteforce
Les lignes produites sont du texte ; aucune connexion reseau n'est effectuee.
IP utilisees : plage de documentation RFC 5737 (203.0.113.0/24).
"""
import argparse
from datetime import datetime

HOST = "srv-lab"
ATTACKER = "203.0.113.50"


def ts():
    return datetime.now().strftime("%b %e %H:%M:%S")


def ssh_bruteforce(n=8):
    users = ["admin", "root", "test", "oracle", "ubuntu", "user", "postgres", "pi"]
    for i in range(n):
        yield (f"{ts()} {HOST} sshd[{2000+i}]: Failed password for invalid user "
               f"{users[i % len(users)]} from {ATTACKER} port {40000+i} ssh2")


def new_user():
    yield (f"{ts()} {HOST} useradd[3100]: new user: name=testuser, UID=1005, "
           f"GID=1005, home=/home/testuser, shell=/bin/bash")


def sudo_root():
    yield (f"{ts()} {HOST} sudo:   analyste : TTY=pts/0 ; PWD=/home/analyste ; "
           f"USER=root ; COMMAND=/bin/bash")


def web_scan(n=12):
    for i in range(n):
        yield (f'{ATTACKER} - - [07/Oct/2026:10:00:{i:02d} +0300] '
               f'"GET /test-path-{i} HTTP/1.1" 400 150 "-" "scanner-test"')


SCENARIOS = {
    "ssh_bruteforce": ssh_bruteforce,
    "new_user": new_user,
    "sudo_root": sudo_root,
    "web_scan": web_scan,
}

if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--scenario", choices=SCENARIOS, required=True)
    args = p.parse_args()
    for line in SCENARIOS[args.scenario]():
        print(line)
