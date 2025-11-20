class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode() 

    # Runtime: O(k) no branching just the length of the word is the number of steps we need to do inside the tree
    # Spacetime: O(1) 
    def addWord(self, word: str) -> None:
        # Check if word in TrieNode
        node = self.root
        for character in word:
            if character not in node.children.keys():
                node.children[character] = TrieNode()
            node = node.children[character]
        node.is_end = True

    # Runtime: O(26 ^ k), k number of dots in the search query because this is where we need to branch
    # Spacetime: O(1)
    def search(self, word: str) -> bool:
        
        def dfs(node, i):
            if i == len(word):
                return node.is_end
                    
            ch = word[i]

            # Case 1: normal character
            if ch != ".":
                if ch not in node.children:
                    return False
                return dfs(node.children[ch], i + 1)

            # Case 2: wildcard '.', try all children
            for child in node.children.values():
                if dfs(child, i + 1):
                    return True
            return False
        
        return dfs(self.root,0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
