
job_id=$(squeue -u bp000231 --noheader -o %A)
echo "job id is $job_id"
node_id=$(scontrol show jobid $job_id | grep -m 1 -o 'nid.\{0,5\}')
echo $node_id > 'nidnr.txt'
echo "node is $node_id"
