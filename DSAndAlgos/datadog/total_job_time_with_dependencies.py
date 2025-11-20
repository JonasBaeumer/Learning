# Recursive version of optimized loop

def find_total_job_time(jobs, job_id):

    # Build up the adj list of format job_id: (time, children)
    adj_list = {job[0]: (job[1],job[2]) for job in jobs}
    
    def dfs(index):
        
        total = adj_list[index][0] 
        for children in adj_list[index][1]:
            total += dfs(children)
        
        return total

    return dfs(job_id)

print(find_total_job_time(jobs, 1))  # 30 + (10+20) + 60 = 120
print(find_total_job_time(jobs, 2))  # 10 + 20 = 30
print(find_total_job_time(jobs, 4))  # 60

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

# How can we improve that? Our list creation is somewhat inefficient, because we have an unordered list (in terms of the position and the relative job_id) thats why we can abstract
# the list into a dict that just consist of the job_id and the time and children ids, then we can 
# simply navigate the list instead of our graph which guarantees O(n)
# Runtime optimized: O(n) -> O(n) build list + O(n/k) worst case -> O(n)
# Space complexity: O(n)

def find_total_job_time(jobs, job_id):

    # Build up the adj list of format job_id: (time, children)
    adj_list = {job[0]: (job[1],job[2]) for job in jobs}
    queue = deque()
    queue.append(job_id)
    total = 0

    while queue:
        # 1. Pop first value 
        value = queue.pop()
        # Find the correct job:
        job = adj_list[value]
        # 2. Look up time and add to total 
        total += job[0]
        # 3. Add children to queue
        for children in job[1]:
            queue.append(children)

    return total

print(find_total_job_time(jobs, 1))  # 30 + (10+20) + 60 = 120
print(find_total_job_time(jobs, 2))  # 10 + 20 = 30
print(find_total_job_time(jobs, 4))  # 60

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
