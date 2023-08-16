from ftplib import FTP

host = "seansama.bplaced.net"
user = "seansama"
with open('text.txt', 'r') as f:
    password = f.read()

with FTP(host) as ftp:
    ftp.login(user=user, passwd=password)
    print(ftp.getwelcome())
