from config import *
import telnetlib

def main():
  try:
    login_device()
    # Cisco command run
    telnet.write("show running-config")
    telnet.read_all()

  except ConnectionRefusedError:
    print("ConnectionRefusedError !!!")

if __name__ == "__main__":
  main()