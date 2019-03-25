def exist(board, word):
	m = len(board)
	n = len(board[0])
	if (m == 0) or (len(word) == 0):
		return False
	for i in range(m):
		for j in range(n):
			if Search_word(board, word, 0, i, j) == True:
				return True
	return False

def Search_word(board, word, pos, i, j):
	m = len(board)
	n = len(board[0])
	if pos == len(word):
		return True
	if board[i][j] != word[pos]:
		return False
	if (i < 0) or (j < 0) or (pos > m * n) or (i >= m) or (j >= n):
		return False
	temp = board[i][j]
	board[i][j] = '*'
	search_word = (Search_word(board, word, pos + 1, i + 1, j) or 
		Search_word(board, word, pos + 1, i - 1, j) or 
		Search_word(board, word, pos + 1, i, j - 1) or 
		Search_word(board, word, pos + 1, i, j + 1))
	board[i][j] = temp
	return search_word
