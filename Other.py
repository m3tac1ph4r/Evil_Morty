import sys
import os
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l" , "--list" , help="Subdomain list" , required=True)
    args = parser.parse_args()
    wayback(args.list)

def wayback(filename):
    print("-" * 30)
    print("WAYBACKURLS") 
    os.system(f"cat {filename} | /opt/waybackurls > WAYBACKURLS.txt")
    print("DONE")
    print("-" * 30)

main()
