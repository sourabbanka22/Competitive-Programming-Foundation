class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol = "*"

    def populateTrieFrom(self, string):
        # Write your code here.
        current = self.root
        for char in string:
            if char not in current:
                current[char] = {}
            current = current[char]
            current[self.endSymbol] = True
        
        current = self.root
        for first in range(len(string)):
            for second in range(first, len(string)):
                if string[second] not in current:
                    current[string[second]] = {}
                current = current[string[second]]
            current[self.endSymbol] = True
            current = self.root
                

    def contains(self, string):
        # Write your code here.
        current = self.root
        for char in string:
            if char not in current:
                return False
            current = current[char]
        
        return self.endSymbol in current

def multiStringSearch(bigString, smallStrings):
    # Write your code here.
    bigStringList = bigString.split(" ")
    trie = Trie()

    for string in bigStringList:
        trie.populateTrieFrom(string)
    
    contains = []

    for string in smallStrings:
        if trie.contains(string):
            contains.append(True)
        else:
            contains.append(False)

    return contains

print(multiStringSearch("this is a big string", ["this", "yo", "is", "a", "bigger", "string", "kappa"]))
