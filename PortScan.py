import os
import sys
import argparse

def main():
    print("=" * 15 + "PORT SCANNER" + "=" * 15)
    parser = argparse.ArgumentParser()
    parser.add_argument("-l" , "--list" , help="List of Ip addresses" , required=True)
    parser.add_argument("-n" , "--nmap" , help="Nmap Scan (SLOW)")
    args = parser.parse_args()
    filename = args.list
    iplist = subtoip(filename)
    ports = masscan(iplist)
    if args.nmap:
        nmap(iplist, ports)


def masscan(filename):
    print("MASSCAN")
    os.system(f"sudo masscan --rate=10000 -iL {filename} -Pn -p1-65535 -oL MASSCAN.txt")
    print("DONE")
    portlist("MASSCAN.txt")
    print("-" * 42)
    return "MASSCAN.txt"

def nmap(filename, ports):
    print("NMAP")
    os.system(f"nmap -T4 -sCV -oN NMAP.txt -iL {filename} -p $(cat {ports})")
    print("-" * 42)
    return "NMAP.txt"

def subtoip(filename):
    print("CONVERTING SUBDOMAINS TO IP")
    os.system("cat " + filename + " | while read line ; do host $line >> tempip ; done ")
<<<<<<< HEAD
    os.system("cat tempip | grep -E '\\b([0-9]{1,3}\.){3}[0-9]{1,3}\\b' | sort -n -t ' ' -k 4 | awk '{print $NF}' |sort| uniq > IPLIST.txt && rm -rf tempip")
=======
    os.system("cat tempip | grep -E '\\b([0-9]{1,3}\.){3}[0-9]{1,3}\\b' | sort -n -t ' ' -k 4 | awk '{print $NF}' |sort |  uniq > IPLIST.txt && rm -rf tempip")
>>>>>>> 7c124bd8defc43d2bccd09daf8d6af6df44b24e0
    print("DONE")
    print("-" * 42)
    return "IPLIST.txt"

def portlist(filename):
    os.system('cat ' + filename + " | awk '/open/ {print $3}' | sort | uniq | tr '\\n' ',' | sed s/.$// > PORTS.txt")
    return "PORTS.txt"


main()
