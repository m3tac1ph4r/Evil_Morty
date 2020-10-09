import sys
import os
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l" , "--list" , help="Subdomain list" , required=True)
    args = parser.parse_args()
    wayback(args.list)
    eyeWitness(args.list)
    s3Scan(args.list)

def wayback(filename):
    print("-" * 30)
    print("WAYBACKURLS") 
    os.system(f"cat {filename} | /opt/waybackurls > WAYBACKURLS.txt")
    print("DONE")
    print("-" * 30)

def eyeWitness(filename):
    print("-" * 30)
    print("EYEWITNESS")
    os.system(f"/opt/EyeWitness/Python/EyeWitness.py -f {filename} --web")
    print("DONE")
    print("-" * 30)

def s3Scan(filename):
    print("-" * 30)
    print("S3-Scan")
    os.system(f"python3 /opt/s3scanner/s3scanner.py --out S3BUCKETS.txt --file {filename}")
    print("DONE")
    print("-" * 30)

main()
