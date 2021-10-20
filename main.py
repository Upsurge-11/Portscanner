import socket
import termcolor


def scan(target, ports):
    print(termcolor.colored(("\n" + "Starting scan for " + str(target)), "cyan"))
    for port in range(1, ports+1):
        scan_port(target, port)


def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print("[+] Port Open " + str(port))
        sock.close()
    except:
        pass


targets = input(termcolor.colored(("[*] Enter targets to scan (split them by , to scan) :- "), "white"))
number_ports = int((input(termcolor.colored(("[*] Enter how many ports you want to scan :- "), "white"))))

if ',' in targets:
    print(termcolor.colored(("[*] Scanning Multiple Targets........."), "red"))
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '), number_ports)
else:
    scan(targets, number_ports)
