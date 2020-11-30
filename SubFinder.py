#!/usr/bin/python3
# Tools to be used
# Amass
# Subfinder
# gobuster
# ffuf
# Massdns

import os
import sys
import requests
import urllib
import argparse

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
def subfinder(target):
    # Enter API Keys
    FILENAME = 'Subdomain-01.txt'
    os.system('/opt/subfinder -dL ' + target + ' --all -nW | tee '+ FILENAME)

# Tested
def amass(target):
    FILENAME = 'Subdomain-02.txt'
    os.system('amass enum -active -df ' + target + ' | tee '+ FILENAME)

def brute(target , wordlist):
    WORDLIST = wordlist
    FILENAME = 'Subdomain-03.txt'
    f = open(target)
    for i in f.readline():
        # Replace with ffuf
        os.system(f'gobuster dns -d {i.strip()} -t 90  -w {WORDLIST} | tee {FILENAME}')

def vhost(target , wordlist):
    WORDLIST = wordlist
    FILENAME = 'Subdomain-04.txt'
    f = open(target)
    for i in f.readline():
        os.system(f'gobuster vhost -u {i.strip()} -w {WORDLIST} | {FILENAME}')


# Tested
def merge():
    os.system('cat Subdomain-0* >> subdomaintemp.txt && rm -rf Subdomain-0*')
    os.system('sort subdomaintemp.txt | uniq > SUBDOMAINS.txt')


# Tested
def main():
    parse = argparse.ArgumentParser()
    parse.add_argument("--target", help="Filename containing target domains")
    parse.add_argument("--wordlist", help="Wordlist for Brute")
    parse.add_argument("--brute" , help="Use Bruteforce" , action="store_true")
    parse.add_argument("--vhost" , help="Use Vhost Scan" , action="store_true")
    args = parse.parse_args()
    target = args.target
    if not args.target:
        parse.print_help()
        sys.exit(0)
    print("SUBDOMAIN SCAN\n"+"="*50)
    if args.brute:
        if not args.wordlist:
            print("Specify Wordlist")
            parse.print_help()
            sys.exit(1)
        print("BRUTEFORCE\n"+"-"*50)
        brute(target ,args.wordlist) 
        merge()
        sys.exit()
    if args.vhost:
        if not args.wordlist:
            print("Specify Wordlist")
            parse.print_help()
            sys.exit()
        print("VHOST\n"+"-"*50)
        vhost(target ,args.wordlist)
        merge()
        sys.exit()

    print("AMASS\n"+"-"*50)
    amass(target)
    print("SUBFINDER\n"+"-"*50)
    subfinder(target)
    print("MERGING\n"+"-"*50)
    merge()

main()
