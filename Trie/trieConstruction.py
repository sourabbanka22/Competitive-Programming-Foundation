# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.
class Trie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
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

class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        # Write your code here.
		current = self.root
		for index1 in range(len(string)):
			for index2 in range(index1, len(string)):
				if string[index2] not in current:
					current[string[index2]] = {}
				current = current[string[index2]]
			current[self.endSymbol] = True
			current = self.root
				

    def containsSuffix(self, string):
        # Write your code here.
		current = self.root
        for char in string:
			if char not in current:
				return False
			current = current[char]
		
		if self.endSymbol in current: 
			return True
		else:
			return False

