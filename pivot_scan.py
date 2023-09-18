import socket
import os
import sys

port_list = [21,22,23,25,53,80,111,139,445,512,513,514,1099,1524,2049,2121,3306,5432,5900,6000,6667,8009]

def ret_banner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except OSError:
        return

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        ip_addresses = []
        for arg in sys.argv[1:]:
            ip_addresses.append(arg)
        for address in ip_addresses:
            _ip = address
            for _port in port_list:
                try:
                    _banner = ret_banner(_ip, _port)
                except:
                    _banner = "error while trying to connect"
                print(f'[*] {address}:{_port} = {_banner}')

    else:
        print(f'[-] Usage: {str(sys.argv[0])} <vuln filename>')
        exit(0)
