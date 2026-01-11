"""
Goal: To help the Elves figure out which path is causing the issue, they need you to find every path from you to out.

Idea: We build a directed graph structure starting from root.
1) We have to transform an input into a dictionary that will help us build the tree sturcture.
Important note: We have a directional graph meaning data can only flow of the direction of the edge and not backwards
2) Then we traverse the tree to find all possible paths inside the tree from "you" to "end"
Important: We need to keep a track of paths we have already visited as well as which path we are currently on to prevent potential 
cycles
"""

"""
This method build a dictionary to represent the tree structure that we can use to traverse the tree
"""
def build_graph(paths: list[str]):
	graph = {}
	for line in paths:
		left, right = line.split(":")
		key = left.strip()
		values = right.strip().split()
		graph[key] = values
	return graph	
	
"""
This method traverses the tree and find all the available paths to target with DFS
"""
from functools import cache
def find_paths_to_end(graph: dict[str, list[str]]):
	
	@cache	
	def dfs(node: str, seen_fft: bool, seen_dac: bool):
		# base case: we found a way to "end"
		if not node:
			return 0
		# base case: we have actually found a valid path
		if node == "out":
			if seen_fft and seen_dac:
				return 1
			else:
				return 0
		if node == "fft":
			seen_fft = True
		elif node == "dac":
			seen_dac = True
		paths = graph[node]
		result = 0
		for path in paths:
			result += dfs(path, seen_fft, seen_dac)
		return result
	
	return dfs("svr", False, False)

test_graph = {
    "aaa": ["you", "hhh"],
    "you": ["bbb", "ccc"],
    "bbb": ["ddd", "eee"],
    "ccc": ["ddd", "eee", "fff"],
    "ddd": ["ggg"],
    "eee": ["out"],
    "fff": ["out"],
    "ggg": ["out"],
    "hhh": ["ccc", "fff", "iii"],
    "iii": ["out"]
}

#print(find_paths_to_end(test_graph))

filepath = "/Users/jonas/Downloads/input-11.txt"
lines = []
with open(filepath, "r") as file:
	for line in file:
		lines.append(line)
graph = build_graph(lines)
print(find_paths_to_end(graph))
