from hbp_nrp_virtual_coach.oidc_http_client import OIDCHTTPClient
from helper_functions import *

client = OIDCHTTPClient(oidc_username="BenediktFeldotto")
auth = {'Authorization': client.get_auth_header()}
base_url = get_sites()['DAINT-CSCS']['url']

print('get information')
# get information about the current user, e.g.
# role, Unix login and group(s)
props = get_properties(base_url, auth)
if not "user" == props['client']['role']['selected']:
    print "Sorry, you do not have a user account at the selected site!\n"
else:
    print props['client']

print('set and submit job')
# set and submit the job
job, inputs = setup_job(1, 10, 5, props, '148.187.97.13', '148.187.97.12')
job_url = submit(base_url+"/jobs", job, auth, inputs)
print "Job {status} at {url}".format(status=get_properties(job_url, auth)['status'], url=job_url)

print('wait for job to finish')
# wait for the job to finish
wait_for_completion(job_url, auth)
#print get_properties(job_url, auth)['status']

print('list files in job working dir')
# list files in job working directory
work_dir = get_working_directory(job_url, auth)
#get_properties(work_dir+"/files", auth)

print('download and show output')
# download and show stdout
print '================= STDOUT ==================='
print get_file_content(work_dir + "/files" + "/stdout", auth)
print '================= STDERR ==================='
print get_file_content(work_dir + "/files" + "/stderr", auth)
