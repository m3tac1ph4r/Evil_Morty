#!/usr/bin/python3

import os
import sys
import requests
import urllib

# Tested
def websites(domain):
    FILENAME = 'Website.txt'
    censys = f'https://censys.io/certificates?q={domain}'
    certsh = f"https://crt.sh/?q={domain}"
    with open(FILENAME , 'a+') as f:
        f.write('-'*50)
        f.write('\n')
        f.write(censys+'\n')
        f.write(certsh+'\n')
        f.write('-'*50)
        f.write('\n')


# Use Domain File
# Tested
def subfinder():
    # Enter API Keys
    FILENAME = 'Domains1.txt'
    os.system('/opt/subfinder-linux-amd64 -dL domains.txt -nW -oI '+ FILENAME)

# Not Tested
def amass():
    FILENAME = 'Domains2.txt'
    os.system('amass intel -active -df domains.txt -o '+ FILENAME)



