class Trie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateTrieFrom(self, string):
        # Write your code here.
		current = self.root
        for char in string:
			if char not in current:
				current[char] = {}
			current = current[char]
		current[self.endSymbol] = True
				

    def contains(self, string):
        # Write your code here.
        pass

def multiStringSearch(bigString, smallStrings):
    # Write your code here.
    bigStringList = bigString.split(" ")
    return bigStringList

print(multiStringSearch("this is a big string", ["this", "yo", "is", "a", "bigger", "string", "kappa"]))
