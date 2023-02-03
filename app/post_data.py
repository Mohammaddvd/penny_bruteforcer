from colorama import Fore

def check(data):
    if(data == None):
        print("\n[-] didnt define data , e.x --data \"username=^USER^&pwd=^PWD^\":err")
        return False, False
    
    if("=" not in data):
        print("\n[-] incorect data , e.x --data \"username=^USER^&pwd=^PWD^\":err")
        return False, False
    
    if(":" not in data):
        print("\nyou didnt define error msg , e.x  --data \"username=^USER^&pwd=^PWD^\":incorect creds")
        return False, False

    data = data.split(":")
    err = data[1]
    data = data[0]

    if("&" not in data):
        print(Fore.YELLOW + "\n[*] Warning your data only have one variable")
        data = data.split("=")
        data = {data[0]:data[1]}
    else:
        d = data.split("&")
        data = {}
        for var in d:
            if("=" not in var):
                print("\n[-] incorect data , e.x --data \"username=^USER^&pwd=^PWD^\":err")
                return False, False
            
            var=var.split("=")
            data.update({var[0]:var[1]})

    print(Fore.GREEN + "\n[+] Data validate")
    return data,err