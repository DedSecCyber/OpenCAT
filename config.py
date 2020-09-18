import telnetlib

user = "admin"
passwd = "Pass"
host = "127.0.0.1"

def login_device():
  telnet = telnetlib.Telnet(host)
  telnet.read_until("Username: ")
  telnet.write(user + "\n")
  telnet.read_until("Password: ")
  telnet.write(passwd + "\n")
