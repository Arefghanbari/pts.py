import socket
import IPy
from pyfiglet import Figlet
Text = Figlet(font='slant')
print(Text.renderText(' LOCKER TEAM'))


def scn(targets):
    converted = link(targets)
    print('\n[*] Scaning targets '+ str(targets))
    for port in range(1,500):
        scan(converted,port)


def link(ip):
    try:
        IP = ip
        return (ip)
    except ValueError:
        return socket.gethostbyname(ip)
def get_ban(s):
    return s.recv(1023)

def scan(ip,port):
    try:
        sock = socket.socket()
        sock.settimeout(0.3)
        sock.connect((ip,port))
        try:
            banner = get_ban(sock)
            print('[+] Port ' + str(port) + 'is open' + ':' + str(banner.decode()))
        except:
            print('[+] Port ' + str(port))
    except:
        pass
targets = input('[+] Enter the targets ip to scan (split the targets ip with , ) : ')
if __name__ == '__main__':
    if ',' in targets:
        for ip_add in targets.split(','):
            scn(ip_add.strip(' '))
    else:
        scn(targets)