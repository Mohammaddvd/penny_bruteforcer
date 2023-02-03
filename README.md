penny-bruteforcer is a simple tool by python for Brute-Forcing attack on services:
-ssh
-mysql
-http-post
-ftp

> python3 penny.py --help
__________
\______   \ ____   ____   ____ ___.__.
 |     ___// __ \ /    \ /    <   |  |
 |    |   \  ___/|   |  \   |  \___  |
 |____|    \___  >___|  /___|  / ____|
               \/     \/     \/\/




usage: penny.py [-h] [-s SERVICE] [-i IP] [--port PORT] [-d DATA] [-c COOKIES]
                [-u USERNAME] [-p PASSWORD] [-U USERNAMES] [-P PASSWORDS]
                [-t THREAD]

options:
  -h, --help            show this help message and exit
  -s SERVICE, --service SERVICE
                        Service name you want to attack , [mysql , ssh , http-post]
  -i IP, --ip IP        Your target ip
  --port PORT           Your target port
  -d DATA, --data DATA  data (for http-post) body e.x
                        'username=^USER^&pwd=^PWD^':incorect creds
  -c COOKIES, --cookies COOKIES
                        cookie value e.x -c 'admin:1'
  -u USERNAME, --user USERNAME
                        Your username ![means that you dont want to define username list]
  -p PASSWORD, --password PASSWORD
                        Your password ![means that you dont want to define password list]
  -U USERNAMES, --users USERNAMES
                        Your username list
  -P PASSWORDS, --passwords PASSWORDS
                        Your password list
  -t THREAD, --thread THREAD
                        max thread , defualt is 30
