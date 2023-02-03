import sys

def chkCookie(cookies):
    f_cookies = {}
    
    if(":" not in cookies):
        print(Fore.RED + "[-] invalid cookies")
        sys.exit()

    cookies = cookies.split("&")

    for c in cookies:
        f_cookies[c.split(":")[0]] = c.split(":")[1]

    return f_cookies