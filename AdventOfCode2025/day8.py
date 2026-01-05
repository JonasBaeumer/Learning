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

def find_all_shortest_pairs(points: list(tuple[int, int, int])) -> list[(tuple[int, int, int], tuple[int, int, int])]:
	heap = []
	for i in range(len(points)):
		for j in range(i + 1, len(points)):
			d = euclidean_distance(points[i], points[j])
			heapq.heappush(heap, (d, i, j))  # min-heap by d
	return heap

"""
Union find class to manager cluster merging and tracking in efficient time
"""
class UnionFind:
	def __init__(self, n):
		self.parent = list(range(n))
		self.size = [1] * n   # size of each component

	def find(self, x):
		if self.parent[x] != x:
			self.parent[x] = self.find(self.parent[x])  # path compression
		return self.parent[x]

	def union(self, x, y):
		root_x = self.find(x)
		root_y = self.find(y)

		if root_x == root_y:
			return False  # already connected

		# union by size
		if self.size[root_x] < self.size[root_y]:
			root_x, root_y = root_y, root_x

		self.parent[root_y] = root_x
		self.size[root_x] += self.size[root_y]
		return True

filepath = '/Users/jonas/Downloads/input-8.txt'
datapoints = []

with open(filepath, "r") as file:
	counter = 0
	for line in file:
		counter += 1
		coordinates = line.strip().split(",")
		coordinates = list(map(lambda x: int(x), coordinates))
		datapoints.append((coordinates[0], coordinates[1], coordinates[2]))

point_index = {p: i for i, p in enumerate(datapoints)}
shortest_pairs = find_all_shortest_pairs(datapoints)

heap = find_all_shortest_pairs(datapoints)

uf = UnionFind(len(datapoints))
number_of_circuits = len(datapoints)
last_merge = None

while heap and number_of_circuits > 1:
	dist, i, j = heapq.heappop(heap)  # always next closest
	if uf.find(i) != uf.find(j):
		uf.union(i, j)
		number_of_circuits -= 1
		last_merge = (i, j)

print(datapoints[last_merge[0]][0] * datapoints[last_merge[1]][0])
