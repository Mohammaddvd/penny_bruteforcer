from app.l_banner import banner as lbanner
from app.w_banner import banner as wbanner
from app.check_up import check_up
from app.check_url import check_url
from app.post_data import check as checkd
from app.port import portCheck
from app.chk_cookie import chkCookie
from services.mysql import Mysql
from services.http_post import Http_Post
from services.ssh import Ssh
from services.ftp import Ftp
from colorama import Fore,init
import sys, os, argparse


if(__name__!="__main__"):
    sys.exit()
else:
    pass

# banner
if(os.name=="nt"):
    init()
    print(Fore.LIGHTRED_EX + wbanner.__doc__)
else:
    print(lbanner.__doc__)


# args
parser = argparse.ArgumentParser()
parser.add_argument("-s","--service",dest="service",help="Service name you want to attack , [mysql , ssh , http-post]")
parser.add_argument("-i","--ip",dest="ip",help="Your target ip")
parser.add_argument("--port",dest="port",help="Your target port", type=int)
parser.add_argument("-d","--data",dest="data",help="data (for http-post) body e.x 'username=^USER^&pwd=^PWD^':incorect creds")
parser.add_argument("-c","--cookies",dest="cookies",help="cookie value e.x -c 'admin:1'")
parser.add_argument("-u","--user",dest="username",help="Your username ![you dont want to define username list]")
parser.add_argument("-p","--password",dest="password",help="Your password ![you dont want to define password list]")
parser.add_argument("-U","--users",dest="usernames",help="Your username list")
parser.add_argument("-P","--passwords",dest="passwords",help="Your password list")
parser.add_argument("-t","--thread",default=30,dest="thread",help="max thread , defualt is 30")
args = parser.parse_args()


# select services

#   mysql

if(args.service=="mysql"):
    u = p = None
    ip = args.ip
    
    if(args.port != None):
        port = portCheck(args.port)
    else:
        port = 3306

    try:    #get username
        if(args.username != None):
            u = [args.username]
        else:
            u = open(args.usernames, "r").read().split("\n")
    except:
        print(Fore.RED + "Cant read your username list , check your file name")
        sys.exit()
    
    try:    #get password
        if(args.password != None):
            p = [args.password]
        else:
            p = open(args.passwords, "r").read().split("\n")
    except:
        print(Fore.RED + "Cant read your password list , check your file name")
        sys.exit()

    #check server is up
    cUp = check_up(ip,port)
    if(cUp):
        print(Fore.GREEN + "[+] Server is up\n" + Fore.WHITE)
    else:
        print(Fore.RED + "Server isnt up , check ip (or default port)")
        sys.exit()
    stt = Mysql(u,p,ip,port,args.thread)


#   http-post


elif(args.service == "http-post"):
    u = p = None
    ip = args.ip
    data = args.data
    ch_data,err = checkd(data)

    if(ch_data != False):   # validation data
        pass
    else:
        sys.exit()

    if(args.cookies == None or args.cookies == ""):
        cookies = {}
    else:
        cookies = chkCookie(args.cookies)

    try:    #get username
        if(args.username != None):
            u = [args.username]
        else:
            u = open(args.usernames, "r").read().split("\n")
    except:
        print(Fore.RED + "Cant read your username list , check your file name")
        sys.exit()
    
    try:    #get password
        if(args.password != None):
            p = [args.password]
        else:
            p = open(args.passwords, "r").read().split("\n")
    except:
        print(Fore.RED + "Cant read your password list , check your file name")
        sys.exit()
    
    #check url and up

    cUp = check_url(ip)
    if(cUp[0]):
        print(Fore.GREEN + "[+] Server is up" + Fore.WHITE)
    else:
        sys.exit()

    try:
        thr = int(args.thread)
    except:
        pass

    stt = Http_Post(cUp[1],u,p,ch_data,err,thr, cookies)



#   ssh



elif(args.service == "ssh"):
    u = p = None
    ip = args.ip

    if(args.port != None):
        port = portCheck(args.port)
    else:
        port = 22

    try:    #get username
        if(args.username != None):
            u = [args.username]
        else:
            u = open(args.usernames, "r").read().split("\n")
    except:
        print(Fore.RED + "Cant read your username list , check your file name")
        sys.exit()
    
    try:    #get password
        if(args.password != None):
            p = [args.password]
        else:
            p = open(args.passwords, "r").read().split("\n")
    except:
        print(Fore.RED + "Cant read your password list , check your file name")
        sys.exit()
    
    cUp = check_up(ip,port) # check up
    if(cUp):
        print(Fore.GREEN + "[+] Server is up\n" + Fore.WHITE)
    else:
        print(Fore.RED + "Server isnt up , check ip (or default port)")
        sys.exit()
    thr = int(args.thread)
    start = Ssh(ip,port,u,p,thr)



#FTP



elif(args.service == "ftp"):
    u = p = None
    ip = args.ip
    if(args.port != None):
        port = portCheck(args.port)
    else:
        port = 21
    try:    #get username
        if(args.username != None):
            u = [args.username]
        else:
            u = open(args.usernames, "r").read().split("\n")
    except:
        print(Fore.RED + "Cant read your username list , check your file name")
        sys.exit()
    
    try:    #get password
        if(args.password != None):
            p = [args.password]
        else:
            p = open(args.passwords, "r").read().split("\n")
    except:
        print(Fore.RED + "Cant read your password list , check your file name")
        sys.exit()
    cUp = check_up(ip,port) # check up
    if(cUp):
        print(Fore.GREEN + "[+] Server is up\n" + Fore.WHITE)
    else:
        print(Fore.RED + "Server isnt up , check ip (or default port)")
        sys.exit()
    thr = int(args.thread)
    # start = Ssh(ip,port,u,p,thr,args.verbose)
    start = Ftp(ip,port,u,p,thr)

else:
    print(Fore.LIGHTBLACK_EX + "didnt define service e.x --service ssh\n\n")
    sys.exit()