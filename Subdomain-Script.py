#!/usr/bin/python3
# Tools to be used
# Amass
# Subfinder
# Massdns

import os
import sys
import requests
import urllib

# Find subdomains manually
def websites(domain):
    FILENAME = 'SUBDOMAIN-MANUAL.txt'
    censys = f'https://censys.io/certificates?q={domain}'
    certsh = f"https://crt.sh/?q={domain}"
    with open(FILENAME , 'a+') as f:
        f.write('-'*50)
        f.write('\n')
        f.write(censys+'\n')
        f.write(certsh+'\n')
        f.write('-'*50)
        f.write('\n')


# Tested
def subfinder():
    # Enter API Keys
    FILENAME = 'Subdomain-01.txt'
    os.system('/opt/subfinder-linux-amd64 -dL target.txt -nW | tee '+ FILENAME)

# Tested
def amass():
    FILENAME = 'Subdomain-02.txt'
    os.system('amass enum -active -df target.txt | tee '+ FILENAME)


def merge():
    os.system('cat Subdomain-0* >> subdomaintemp.txt')
    os.system('sort subdomaintemp.txt | uniq > SUBDOMAINS.txt')


def main():
    print("Subdomains")
    amass()
    subfinder()
    print("Done")
    print("Merging")
    merge()

main()

