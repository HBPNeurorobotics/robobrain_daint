filename='nidnr.txt'
while read line; do
nid=$line
done < $filename

echo "nid is : $nid"

ssh -A $nid
