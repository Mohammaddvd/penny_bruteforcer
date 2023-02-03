from requests import *
from colorama import Fore

def check_url(url):

    print(Fore.YELLOW + "[*] remember that you should define path in --ip or -i , e.x 127.0.0.1/test.php")

    if(url == None):
        print(Fore.RED + "\n[-] invalid url , or its down")
        return [False]

    if(url[0:8] == "https://"):
        pass
    elif(url[0:7] == "http://"):
        pass
    else:
        if(":443" in url):
            url = "https://"+url
        else:
            url = "http://"+url

    try:
        req = get(url, timeout=5)
        if(req.status_code == 200 or req.status_code == 301):
            return [True,url]
        else:
            print(Fore.RED + "\n[-] invalid url , or its down")
            return [False]
    except:
        print(Fore.RED + "\n[-] invalid url , or its down")
        return [False]