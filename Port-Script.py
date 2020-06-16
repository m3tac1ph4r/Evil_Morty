#!/usr/bin/python3
import os
import sys

def masscan(ip):
    os.system(f'masscan -Pn --max-rate=1000 -p1-65535 -oL ../Ports/{ip}.ports.raw.txt')
    nmap(ip)

def nmap(ip):
    portList = ''# Create a port list from port scan
    os.system(f'nmap -sC -Pn -sV -p {portList} -oN ../Ports/{ip}.VERSION.txt {ip}')

def portMain():
    FILENAME = 'ip.txt'
    f = open(FILENAME)
    lines = f.readlines()
    for line in lines:
        masscan(line)

    f.seek(0)
    lines = f.readlines()
    for line in lines:
        nmap(ip)

    f.close()



portMain()

