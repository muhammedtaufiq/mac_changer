#!/usr/bin/env python

import subprocess

subprocess.call(" ifconfig ", shell=True)#runs"ifconfig listing all interfaces

interface = (input("please input the interface:"))# Select the interface to be changed
new_mac = (input("Please enter 12 digit Mac eg 11:22:33:44:55:66 :"))# Select the MAC address to be ammended to.

print("[+] Changing MAC Address for " + interface + " to " + new_mac),


subprocess.call(" ifconfig " + interface + " down ", shell=True)#runs"ifconfig to bring adapter Down"
subprocess.call(" ifconfig " + interface + " hw " " ether " + new_mac, shell=True)#changes the Mac address"
subprocess.call(" ifconfig " + interface + " up ", shell=True) #Brings up the adapter"

print("[+] MAC Address for " + interface + " is now changed to " + new_mac)
