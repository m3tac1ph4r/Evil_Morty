# Port Scan
nmap -sC -sV -Pn -v -p `cat ports.txt` -oA Report $target
masscan --max-rate=1000 -Pn -p1-65535 -vv -oX Ports $target

# Subdomains
amass enum -active -df domains.txt -o subdomains1.txt
subfinder -dL domains.txt -nW -o subdomains2.txt
gobuster dns -d $target -i -t 90 -v -w $wordlist -o subdomains3.txt
gobuster vhost -u erev0s.com -w awesome_wordlist.txt -o subdomains4.txt

# Combine subdomains
cat sub1.txt >>  temp.txt
cat sub2.txt >>  temp.txt
cat sub3.txt >>  temp.txt
cat sub4.txt >>  temp.txt
sort
uniq

# Get Ip from subdomains
awk '/[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}/ {print $NF}' 
# Misc
