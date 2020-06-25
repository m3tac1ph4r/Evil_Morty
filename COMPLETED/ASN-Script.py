# DONE
# Create a Name.txt file and put the name of the company therE
import os
import requests
import sys

def asn(name):
    filename = 'Data_ASN'
    f = open(filename,'w+')
    f.write(f'ASNs : {name.upper()}')
    f.write('\n')
    f.write("Whois: https://whois.arin.net/ui/query.do\n")
    f.write("Rips: https://apps.db.ripe.net/db-web-ui/fulltextsearch\n")
    f.write(f"BGP: https://bgp.he.net/search?search%5Bsearch%5D={name}&commit=Search\n")
    f.write("Reverse: https://reverse.report/\n")
    f.write(f"Shodan: https://www.shodan.io/search?query=org%3A%22{name}%22\n")
    f.write('-'*70)
    f.write('\n')
    f.close()


def aqu(name):
    filename = 'Data_Aquasitions'
    f = open(filename,'w+')
    f.write(f"Aquasitions: {name.upper()}")
    f.write('\n')
    f.write(f"Wikipedia: https://en.wikipedia.org/wiki/{name}\n")
    f.write(f"Crunchbase: https://www.crunchbase.com/organization/{name}\n")
    f.write(f"BuiltWith: https://trends.builtwith.com/framework/{name}\n")
    f.write(f"Wikipedia: https://en.wikipedia.org/wiki/{name}\n")
    f.write('-'*70)
    f.write('\n')

    f.close()


def s1_main():
    FILENAME = 'Name.txt'
    f = open(FILENAME)
    name = f.readline().strip()
    print('-'*70)
    print("Searching for "+ name.upper() )
    print("Done")
    print('-'*70)
    asn(name)
    aqu(name)
    f.close()

if __name__ == "__main__":
    s1_main()

