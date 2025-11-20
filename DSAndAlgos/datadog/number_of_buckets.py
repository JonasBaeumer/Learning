# Runtime: O(n), we directly calculate the position where the bucket should be placed
# Spacetime: O(k)

def calc_buckets(latencies, number_of_buckets, bucket_width):
    
    # Build the number of buckets
    buckets = [0 for i in range(number_of_buckets)]

    # Loop over latencies
    for latency in latencies: 

        max_bucket_start = (number_of_buckets - 1) * bucket_width
        index_to_put = int(latency / bucket_width)

        if latency >= max_bucket_start:
            buckets[number_of_buckets - 1] += 1
        else:
            buckets[index_to_put] += 1
    
    return buckets

"""
Question:
Given:
- a list of positive integer latencies
- a number of buckets
- a bucket width

Return a list where each bucket contains the count of latencies
that fall into that latency range.

Bucket i corresponds to:
    [i*bucket_width, (i+1)*bucket_width - 1]
The last bucket includes everything >= (number_of_buckets - 1) * bucket_width
"""
# Runtime: O(k) + O(n) * O(k) -> O(n * k), n number of latencies, k is the number of buckets
# Spacetime: O(k)

def calc_buckets(latencies, number_of_buckets, bucket_width):
    
    # Build the number of buckets
    buckets = [0 for i in range(number_of_buckets)]

    # Loop over latencies
    for latency in latencies: 

        # For each latency, decide on which bucket to increase the score
        for i in range(len(buckets)):
            min = i*bucket_width
            max = (i+1)*bucket_width - 1
            if i == len(buckets)-1:
                buckets[i] += 1
                break
            if min <= latency <= max:
                buckets[i] += 1
                break
    
    return buckets


# -------------------------
# Example test execution
# -------------------------

if __name__ == "__main__":
    latencies = [
        90, 11, 3, 35, 17, 28, 64, 53, 52, 87, 63, 46, 40, 50, 31, 92,
        45, 32, 22, 54, 87, 108, 62, 33, 87, 12, 67, 56, 94, 119, 96,
        23, 21, 25, 86, 5, 32, 77, 3, 16, 8, 61, 105, 88, 49, 57, 114,
        118, 20, 79, 44, 55, 113, 23, 13, 86, 16, 81, 1, 111, 84, 76,
        24, 54, 110, 7, 100, 40, 3, 37, 96, 37, 67, 48, 79, 47, 108,
        36, 15, 112, 37, 13, 40, 66, 39, 110, 47, 87, 34, 50, 55, 112,
        70, 88, 2, 86, 110, 20, 2, 57
    ]

    result = calc_buckets(latencies, 11, 10)

    # Pretty print
    for i, count in enumerate(result):
        if i < 10:
            print(f"{i*10}-{i*10+9}: {count}")
        else:
            print(f"{i*10}+: {count}")
