# Idea to build the graph we can use a hashmap to generate an adjacency list based on the prerequisited
# which will serve as the graph structure we can traverse to detect cycles
# Then we can traverse the graph to detect if we will run into cycles 
# We need to keep an extra list to track which nodes we are curently exploring,
# which nodes we have explored, and which ones are not explored.
# Runtime: O(n) to generate Adjacency list + m to go through all nodes, m = num_courses = O(n+m)
# Spacetime: O(n+m)

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # Build adjacency list to capture the graph 
        # Logic [0, 1], course 1 is a prerequisite to 0

        adj_list= {}

        for prereq in prerequisites:
            if prereq[1] in adj_list:
                adj_list[prereq[1]].append(prereq[0])
            else:
                adj_list[prereq[1]] = [prereq[0]]

        # We keep a list to track the state of our different course nodes
        # 0 -> Not visited, 1 -> Currently visited, 2 -> Already seen
        node_status = [0] * numCourses

        # Should return True if is has a cycle
        def dfs(node):
            # Base case 1: We have a cycle
            if node_status[node] == 1:
                node_status[node] = 2
                return True
            # Base case 2: We have already explored this path before
            if node_status[node] == 2:
                return False
            # Base case 3: We have reached a leaf node
            if node not in adj_list:
                node_status[node] = 2
                return False
            
            # We set the current node to be part of the path we are currently exploring 
            node_status[node] = 1
            has_cycle = False

            for next_step in adj_list[node]:
                print(next_step)
                has_cycle = has_cycle or dfs(next_step)
            
            # When we have finished exploring we will set our node to visit
            node_status[node] = 2

            return has_cycle    
        
        print(adj_list)
        has_cycle = False
        for key in adj_list.keys():
            print(key)
            has_cycle = has_cycle or dfs(key)
        
        return not has_cycle
