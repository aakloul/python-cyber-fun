"""
MacOSX
    sudo ln -s /System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport /usr/local/bin/airport
    # monitor mode on channel 1
    sudo airport en0 sniff 1
    # search for active channels
    sudo airport en1 -s

LINUX
    iwconfig wlan0mon channel 1
"""
import os
import sys
from threading import Thread
import time

import pandas
from scapy.layers.dot11 import Dot11, Dot11Beacon, Dot11Elt, sniff


# initialize the networks dataframe that will contain all access points nearby
networks = pandas.DataFrame(
    columns=["BSSID", "SSID", "dBm_Signal", "Channel", "Crypto"]
)
# set the index BSSID (MAC address of the AP)
networks.set_index("BSSID", inplace=True)


def callback(packet):
    if packet.haslayer(Dot11Beacon):
        # extract the MAC address of the network
        bssid = packet[Dot11].addr2
        # get the name of it
        ssid = packet[Dot11Elt].info.decode()
        try:
            dbm_signal = packet.dBm_AntSignal
        except:
            dbm_signal = "N/A"
        # extract network stats
        stats = packet[Dot11Beacon].network_stats()
        # get the channel of the AP
        channel = stats.get("channel")
        # get the crypto
        crypto = stats.get("crypto")
        networks.loc[bssid] = (ssid, dbm_signal, channel, crypto)


def print_all():
    while True:
        os.system("clear")
        print(networks)
        time.sleep(0.5)


def change_channel():
    ch = 1
    while True:
        # os.system(f"iwconfig {interface} channel {ch}")
        os.system(f"airport {interface} sniff {ch}")
        # switch channel from 1 to 14 each 0.5s
        ch = ch % 14 + 1
        time.sleep(0.5)


if __name__ == "__main__":
    # interface name, check using iwconfig
    interface = sys.argv[1]
    # start the thread that prints all the networks
    printer = Thread(target=print_all)
    printer.daemon = True
    printer.start()
    # start the channel changer
    channel_changer = Thread(target=change_channel)
    channel_changer.daemon = True
    channel_changer.start()
    # start sniffing
    sniff(prn=callback, iface=interface)
