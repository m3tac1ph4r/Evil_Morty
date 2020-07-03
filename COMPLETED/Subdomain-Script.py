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

def brute():
    WORDLIST = ''
    FILENAME = 'Subdomain-03.txt'
    TARGET = 'target.txt'
    f = open('target.txt')
    for i in f.readline():
        os.system(f'gobuster dns -d {i.strip()} -i -t 90 -v -w {WORDLIST} | tee {FILENAME}')

def vhost():
    WORDLIST = ''
    FILENAME = 'Subdomain-04.txt'
    TARGET = 'target.txt'
    f = open('target.txt')
    for i in f.readline():
        os.system(f'gobuster vhost -u {i.strip()} -w {WORDLIST} | {FILENAME}')


# Tested
def merge():
    os.system('cat Subdomain-0* >> subdomaintemp.txt')
    os.system('sort subdomaintemp.txt | uniq > SUBDOMAINS.txt')


# Tested
def main():
    print("Subdomains")
    amass()
    subfinder()
    brute() 
    vhost()
    print("Merging")
    merge()

main()
