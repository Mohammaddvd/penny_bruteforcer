penny-bruteforcer is a simple tool by python for Brute-Forcing attack on services:<br />
-ssh<br />
-mysql<br />
-http-post<br />
-ftp<br />

> python3 penny.py --help<br />
__________<br />
\______   \ ____   ____   ____ ___.__.<br />
 |     ___// __ \ /    \ /    <   |  |<br />
 |    |   \  ___/|   |  \   |  \___  |<br />
 |____|    \___  >___|  /___|  / ____|<br />
               \/     \/     \/\/<br />
<br />
<br />


usage: penny.py [-h] [-s SERVICE] [-i IP] [--port PORT] [-d DATA] [-c COOKIES]<br />
                [-u USERNAME] [-p PASSWORD] [-U USERNAMES] [-P PASSWORDS]<br />
                [-t THREAD]<br />
<br />
options:<br />
  -h, --help            show this help message and exit<br />
  -s SERVICE, --service SERVICE<br />
                        Service name you want to attack , [mysql , ssh , http-post]<br />
  -i IP, --ip IP        Your target ip<br />
  --port PORT           Your target port<br />
  -d DATA, --data DATA  data (for http-post) body e.x<br />
                        'username=^USER^&pwd=^PWD^':incorect creds<br />
  -c COOKIES, --cookies COOKIES<br />
                        cookie value e.x -c 'admin:1'<br />
  -u USERNAME, --user USERNAME<br />
                        Your username ![means that you dont want to define username list]<br />
  -p PASSWORD, --password PASSWORD<br />
                        Your password ![means that you dont want to define password list]<br />
  -U USERNAMES, --users USERNAMES<br />
                        Your username list<br />
  -P PASSWORDS, --passwords PASSWORDS<br />
                        Your password list<br />
  -t THREAD, --thread THREAD<br />
                        max thread , defualt is 30<br />
