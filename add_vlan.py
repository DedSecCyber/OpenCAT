from config import *
import telnetlib
import sys

def main(vlan, vlan_name, interface, interface2):
  try:
    login_device()
    # Cisco command run
    telnet.write("enable\n")
    telnet.write("config terminal\n")
    telnet.write("vlan " + vlan + "\n")
    telnet.write("name " + vlan_name + "\n")
    telnet.write("exit\n")

    if len(sys.argv) == 5:
      telnet.write("interface range " + interface + "-" + interface2)

    if len(sys.argv) == 4:
      telnet.write("interface range " + interface)

    telnet.write("switchport access vlan " + vlan + "\n")
    telnet.write("show vlan brief\n")

    telnet.read_all()

  except ConnectionRefusedError:
    print("ConnectionRefusedError !!!")

if len(sys.argv) != 4:
  print("Usage : " + sys.argv[0] + " <Vlan Number> <Vlan Name> <Start Interface Range> <End Interface Range>")
  sys.exit()

if len(sys.argv) == 4:
  main(sys.argv[1], sys.argv[2], sys.argv[3])

if len(sys.argv) == 5:
  main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

