"""
The problem requires careful consideration of data structures, in particular we need two datastructures that:
1) Allows to quickly calculate and determine the distance between pairs (and also allows us to find the 1000 lowest pairs
2) We can use to track our current circuits (we start with single circuits) and then continously merge circles (as well as
look up if specific pairs are already part of a respective circuit
"""

import math
# Helper function to calculate the Euclidean distance for 3d points:
def euclidean_distance(a: tuple[int, int, int], b: tuple[int, int, int]) -> int:
	return math.dist(a, b)

"""
Approach: 
Since we only have approx 1000 data points, we can brute force compute all of our distances. While doing so we keep a max heap of 1000
shortest pairs.

Since we are using a max heap our root (the max node) is actually the worst of the 1000 elements. This way we can easily determine
wether a new distance should be inserted into the tree or not (only if < root). 
For the first 1000 distance we directly push them into the tree.  
"""
import heapq

def find_1000_shortest_pairs(points: list(tuple[int, int, int])) -> list[(tuple[int, int, int], tuple[int, int, int])]:
	heap = []
	for i in range(len(points)):
		for j in range(i + 1, len(points)):
			distance = euclidean_distance(points[i], points[j])
			# while we have less than 1000 distances stored we always add
			if len(heap) < 1000:
				heapq.heappush(heap, (-distance, points[i], points[j]))
			else:
				if distance < -heap[0][0]:
					heapq.heapreplace(heap, (-distance, points[i], points[j]))
	return [(-neg_d, a, b) for (neg_d, a, b) in heap]

"""
Euclidean distance with 3d points: sqrt( (x1-x2)^2 + (y1-y2)^2 + (z1-z2)^2 )

"""
#def union_merge():

filepath = '/Users/jonas/Downloads/input-8.txt'
datapoints = []

with open(filepath, "r") as file:
	counter = 0
	for line in file:
		counter += 1
		coordinates = line.strip().split(",")
		coordinates = list(map(lambda x: int(x), coordinates))
		datapoints.append((coordinates[0], coordinates[1], coordinates[2]))

print(find_1000_shortest_pairs(datapoints))
