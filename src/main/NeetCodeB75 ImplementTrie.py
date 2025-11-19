# Runtime: O(n), n length of the word we are looking up
# Space: O(26 * n), n length of the longest word

class Trie:

    def __init__(self):
        self.children = {}
        # This is needed to mark wether an explicit word has been inserted 
        # because search only return true if the actual word has been inserted not just the path 
        # Example: 'dog', search('do') should return false
        self.is_end = False
        

    def insert(self, word: str) -> None:
        if not word:
            self.is_end = True
            return 
        
        first = word[0]

        if first not in self.children:
            self.children[first] = Trie()

        self.children[first].insert(word[1:])
        

    def search(self, word: str) -> bool:
        # Traverse the tree to find if the word is there
        if not word:
            if self.is_end: return True
            else: return False
        
        first = word[0]
        if first not in self.children:
            return False
        else:
            return self.children[first].search(word[1:])
        return False
        

    def startsWith(self, prefix: str) -> bool:
        # Traverse the tree to find if the word is there
        if not prefix:
            return True
        
        if prefix[0] not in self.children:
            return False
        else:
            return self.children[prefix[0]].startsWith(prefix[1:])
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
