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
	

filepath = "/Users/jonas/Downloads/input-11.txt"
lines = []
with open(filepath, "r") as file:
	for line in file:
		lines.append(line)
graph = build_graph(lines)
print(graph)	 
