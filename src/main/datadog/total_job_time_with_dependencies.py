# Given an array describing jobs in a build system and a job ID,
# determine the total time required to complete this job.

jobs = [
    # job_id, job_time, child_job_ids
    [1, 30, [2, 4]],
    [2, 10, [3]],
    [4, 60, []],
    [3, 20, []],
]

from collections import deque

def get_job(jobs, id):
    for job in jobs:
        if job[0] == id:
            return job
    raise RuntimeError(f"Job {id} not found")

print(get_job(jobs, 1))
print(get_job(jobs, 4))

# Runtime: O(n^2), worst case iterate through all jobs, for each iteration need to iterate the whole list to find Job, normal case O(k*n), k number of jobs reachable from start
# Spacetime: O(n), queue

def find_total_job_time(jobs, job_id):

    queue = deque()
    queue.append(job_id)
    total = 0

    while queue:
        # 1. Pop first value 
        value = queue.pop()
        # Find the correct job:
        job = get_job(jobs, value)
        # 2. Look up time and add to total 
        total += job[1]
        # 3. Add children to queue
        for children in job[2]:
            queue.append(children)

    return total

print(find_total_job_time(jobs, 1))  # 30 + (10+20) + 60 = 120
print(find_total_job_time(jobs, 2))  # 10 + 20 = 30
print(find_total_job_time(jobs, 4))  # 60
