class WordDictionary:

    # Runtime: O(1)
    # Space: O(1)
    def __init__(self):
        self.children = {}
        self.is_end = False

    # recursive search if character is present if not add it
    # Runtime: O(k), k length of word to be added 
    # Spacetime: O(k), k length of word to be added
    def addWord(self, word: str) -> None:
        # base case, have added the full word
        if not word:
            self.is_end = True
            return
        
        # Check if character has been added
        character = word[0]
        # if yes -> continue search on next level 
        if character not in self.children:
            self.children[character] = WordDictionary()
        # if no -> add it and then continue search
        self.children[character].addWord(word[1:])
    
    # Runtime: O(k * 26 ^ l), k length of word, l number of dots
    # Spacetime: O(k)
    def search(self, word: str) -> bool:
        # base case: have explored the path and need to check wether this
        # exact word has been stored
        if not word:
            return self.is_end
        
        # Check if first character is in children
        character = word[0]
        print(self.children)
        # If yes -> check if character has dot, if dot need to explore any tree
        if character == '.':
            for char in self.children.keys():
                return any(child.search(word[1:]) for child in self.children.values())
        elif character in self.children:
            return self.children[character].search(word[1:])
        # If no -> Stop and return False
        return False
