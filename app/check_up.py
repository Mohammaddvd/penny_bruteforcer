from socket import *

#check server is up
def check_up(ip,port):
    try:
        connection = socket(AF_INET,SOCK_STREAM)
        connection.settimeout(5)
        res = connection.connect_ex((ip, port))

        if(res == 0):
            return True
        
        else:
            return False
            
    except:
        return False