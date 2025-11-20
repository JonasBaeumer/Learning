# 1. Generate set of edges
# 2. Generate our adjacency list
# 3. Traverse graph to generate order of alphabet
# 3a. We have a cycle in our graph (no order is valid)
# 3b. Disconnected graphs are not invalid, meaning we just can just append them at the end of our string

# Order is invalid, two possibilites:
# 1. We have a cycle the break the order assumption, example a < b < c < a
# 2. We have an invalid dictionary words which violates our order assumption and cant be used to derive order

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # 1. Generate our set of edges for building the adjacency list:
        # -> first letter where a and b are different is considered smaller in a that means edge from that letter to the other
        adj = defaultdict(set)
        all_chars = set()

        # Collect all characters (including disconnected)
        for word in words:
            for char in word:
                all_chars.add(char)

        # Step 2: Build the graph by comparing adjacent words
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            # Invalid case: prefix problem
            if word1.startswith(word2) and len(word1) > len(word2):
                return ""

            # Find first differing character
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    adj[word1[j]].add(word2[j])
                    break

        visited = {}  # 0 = unvisited, 1 = visiting, 2 = visited
        result = []
        has_cycle = False

        def dfs(node):
            nonlocal has_cycle
            if node in visited:
                if visited[node] == 1:  # cycle detected
                    has_cycle = True
                return

            visited[node] = 1  # mark as visiting
            for neighbor in adj[node]:
                dfs(neighbor)
            visited[node] = 2  # mark as visited
            result.append(node)  # post-order

        for char in all_chars:
            if char not in visited:
                dfs(char)
            if has_cycle:
                return ""

        result.reverse()
        return "".join(result)
