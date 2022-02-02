class Solution:
    def wordSearch(self, board, word):
        if not board:
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.helper(board,word,i,j):
                    return True
        
        return False
    
    
    def helper(self,board,word,i,j,pos=0):
        if pos == len(word):
            return True
        
        if i < 0 or i >=len(board) or j<0 or j >= len(board[0]) or board[i][j] == '#' or board[i][j] != word[pos]:
            return False
        
        board[i][j] = '#'
        res = self.helper(board,word[pos],i,j+1,pos+1) or self.helper(board,word[pos],i,j-1,pos+1) or self.helper(board,word[pos],i+1,j,pos+1) or self.helper(board,word[pos],i-1,j,pos+1)
        board[i][j] = word[pos]
        return res	


def main():
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCB"
    sol = Solution()
    print(sol.wordSearch(board,word))
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "SEE"
    print(sol.wordSearch(board,word))


if __name__ == "__main__":
    main()