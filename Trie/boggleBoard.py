class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol = "*"

    def populateSuffixTrieFrom(self, string):
        # Write your code here.
        current = self.root
        for char in string:
            if char not in current:
                current[char] = {}
            current = current[char]
        current[self.endSymbol] = string


def boggleBoard(board, words):
    # Write your code here.
    trie = Trie()
    result = set()

    for word in words:
        trie.populateSuffixTrieFrom(word)
    
    visited = [[False for col in board[0]] for row in board]
    for row in range(len(board)):
        for col in range(len(board[0])):
            current = trie.root
            if board[row][col] in trie.root:
                current = current[board[row][col]]
            findMatch(row, col, current, board, visited, result)

    return list(result)

def findMatch(row, col, current, board, visited, result):

    visited[row][col] = True
    unVisitedNodes = getUnVisitedNodes(board, visited, row, col)
    
    if "*" in current:
        result.add(current["*"])

    for node in unVisitedNodes:
        if board[node[0]][node[1]] in current:
            findMatch(node[0], node[1], current[board[node[0]][node[1]]], board, visited, result)
    
    visited[row][col] = False
    return
					
def getUnVisitedNodes(board, visited, row, col):
	unVisited = []
	
	if row - 1 >= 0 and col - 1 >= 0 and not visited[row - 1][col - 1]:
		unVisited.append([row - 1, col - 1])
	
	if row - 1 >= 0 and not visited[row - 1][col]:
		unVisited.append([row - 1, col])
	
	if row - 1 >= 0 and col + 1 < len(board[0]) and not visited[row - 1][col+1]:
		unVisited.append([row - 1, col + 1])
		
	if col + 1 < len(board[0]) and not visited[row][col+1]:
		unVisited.append([row, col + 1])
	
	if row + 1 < len(board) and col + 1 < len(board[0]) and not visited[row + 1][col + 1]:
		unVisited.append([row + 1, col + 1])
		
	if row + 1 < len(board) and not visited[row + 1][col]:
		unVisited.append([row + 1, col])
	
	if row + 1 < len(board) and col - 1 >= 0 and not visited[row + 1][col-1]:
		unVisited.append([row + 1, col - 1])
	
	if col - 1 >= 0 and not visited[row][col-1]:
		unVisited.append([row, col - 1])
	
	return unVisited
	

print(boggleBoard([
  ["t", "h", "i", "s", "i", "s", "a"],
  ["s", "i", "m", "p", "l", "e", "x"],
  ["b", "x", "x", "x", "x", "e", "b"],
  ["x", "o", "g", "g", "l", "x", "o"],
  ["x", "x", "x", "D", "T", "r", "a"],
  ["R", "E", "P", "E", "A", "d", "x"],
  ["x", "x", "x", "x", "x", "x", "x"],
  ["N", "O", "T", "R", "E", "-", "P"],
  ["x", "x", "D", "E", "T", "A", "E"]
],[
  "this",
  "is",
  "not",
  "a",
  "simple",
  "boggle",
  "board",
  "test",
  "REPEATED",
  "NOTRE-PEATED"
]))
print(boggleBoard([["a", "b"], ["c", "d"]],["abcd", "abdc", "acbd", "acdb", "adbc", "adcb", "abca"]))