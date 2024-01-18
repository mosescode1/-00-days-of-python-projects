# EXTEACTING IP4 AND IP6 AND MAC ADDRESS
interface = '''wlo1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.0.105  netmask 255.255.255.0  broadcast 192.168.0.255
        inet6 fe80::6ec6:fea5:4a08:33ae  prefixlen 64  scopeid 0x20<link>
        ether 14:13:33:ee:9c:1b  txqueuelen 1000  (Ethernet)
        RX packets 1007942  bytes 902567350 (902.5 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 531217  bytes 158518152 (158.5 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0'''

splitted = interface.splitlines()
# print(splitted)
# print()
ip_mac = []
for line in splitted[1:4]:
    temp_line = line.split()
    ip_mac.append(temp_line[1])
print(ip_mac)

string = ",".join(ip_mac)
print(string)