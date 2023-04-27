import subprocess

interface = "eth0"
mac_adress = "12:33:44:66:77:88"
print("my_mac_changer started!")

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", mac_adress])
subprocess.call(["ifconfig", interface, "up"])

