# Word-Search
Given an m x n grid of characters board and a string word, return true if word exists in the grid.  The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Straight forward DFS code without using extra memory for creating a visited array/dict.

The helper has one base conditions - If the row or columns are outside the boundary, or if value = '#' or if the value is not equal to the word we are searching for.

Then we set the matrix value to #. We do this to avoid revisiting the nodes.

Then we check the values above,below,right and left of that matrix cell to find the next element of the search_word. If all the letters of the search_word are found then we return TRUE else FALSE.

<img width="466" alt="Screen Shot 2022-02-02 at 4 49 56 PM" src="https://user-images.githubusercontent.com/89628033/152251274-1c8b62b6-9a53-435b-ace1-85ae4a174375.png">

<img width="457" alt="Screen Shot 2022-02-02 at 4 50 01 PM" src="https://user-images.githubusercontent.com/89628033/152251278-cbb92f7c-cf69-41e4-8549-abd4b8e81f63.png">


