# Penny-Bruteforcer

**Penny-Bruteforcer** is a simple Python tool designed for performing brute-force attacks on various services:

- SSH
- MySQL
- HTTP POST
- FTP

## Installation

Ensure you have Python 3 installed, then clone the repository and navigate to the project directory:

```
git clone https://github.com/Mohammaddvd/penny_bruteforcer
cd penny-bruteforcer
```

## Usage

To see the available options and usage instructions, run:

```
python3 penny.py --help
```

### Example Usage

```
python3 penny.py -s ssh -i 192.168.1.1 --port 22 -U usernames.txt -P passwords.txt -t 50
```

## Command Options

```
usage: penny.py [-h] [-s SERVICE] [-i IP] [--port PORT] [-d DATA] [-c COOKIES] [-u USERNAME] [-p PASSWORD] [-U USERNAMES] [-P PASSWORDS] [-t THREAD]

Options:
  -h, --help                  Show this help message and exit
  -s SERVICE, --service SERVICE  
                              Specify the service to attack [mysql, ssh, http-post]
  -i IP, --ip IP              Target IP address
  --port PORT                 Target port
  -d DATA, --data DATA        For HTTP POST, specify the body (e.g., 'username=^USER^&pwd=^PWD^':incorrect creds)
  -c COOKIES, --cookies COOKIES  
                              Cookie value (e.g., -c 'admin:1')
  -u USERNAME, --user USERNAME  
                              Single username (if not using a list)
  -p PASSWORD, --password PASSWORD  
                              Single password (if not using a list)
  -U USERNAMES, --users USERNAMES  
                              File containing a list of usernames
  -P PASSWORDS, --passwords PASSWORDS  
                              File containing a list of passwords
  -t THREAD, --thread THREAD  
                              Maximum number of threads (default is 30)
```

---

Let me know if you need further modifications or additions!
