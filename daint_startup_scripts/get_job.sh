echo " ==== Requestion Job for $1 hours ====" 

if [ -z "$1" ]; then
  echo "--- duration in hours not defined: set as parameter ---"
  exit
else

  salloc -N1 -C 'mc&startx' -A ich004m --time=$1:00:00 --mem=120GB

  job_id=$(squeue -u bp000231 --noheader -o %A)
  echo "job id is $job_id"
  node_id=$(scontrol show jobid 28898554 | grep -m 1 -o 'nid.\{0,4\}')
  echo $node_id > 'nidnr.txt'
  echo "node is $node_id"
fi
