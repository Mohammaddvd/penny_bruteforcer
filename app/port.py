import sys
from colorama import Fore

def portCheck(port):
    try:
        port = int(port)
    except:
        print(Fore.RED + "[-] The port must be number")
        sys.exit()

    if(0<=port<=65535):
        return port
    else:
        print(Fore.RED + "[-] The port must be in range 1-65535")
        sys.exit()