cat domain.txt | while read line
do
  host $line >> temp.txt
done

awk '/[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}/ {print $NF}' temp.txt
