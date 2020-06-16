import os
import requests
import sys

def asn(name):
    print(f'ASNs : {name.upper()}')
    print()
    print("Whois: https://whois.arin.net/ui/query.do")
    print("Rips: https://apps.db.ripe.net/db-web-ui/fulltextsearch")
    print(f"BGP: https://bgp.he.net/search?search%5Bsearch%5D={name}&commit=Search")
    print("Reverse: https://reverse.report/")
    print(f"Shodan: https://www.shodan.io/search?query=org%3A%22{name}%22")
    print('-'*70)


def aqu(name):
    print(f"Aquasitions: {name.upper()}")
    print()
    print(f"Wikipedia: https://en.wikipedia.org/wiki/{name}")
    print(f"Crunchbase: https://www.crunchbase.com/organization/{name}")
    print(f"BuiltWith: https://trends.builtwith.com/framework/{name}")
    print('-'*70)
    print()


def s1_main():
    FILENAME = '../Data/Name.txt'
    f = open(FILENAME)
    name = f.readline().strip()
    print(name.upper())
    print('-'*70)
    asn(name)
    aqu(name)
    f.close()

if __name__ == "__main__":
    s1_main()

