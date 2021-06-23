#!/usr/bin/env python
# coding: utf-8

# In[180]:



#Function to check if Queen is Safe at given position
def isSafe(board,row,col):
    N =len(board)
    #Checking above rows in same column
    for i in range(row):
        if(board[i][col]):
            return False
    
    #right diagonal
    for i,j in zip(range(row,-1,-1), range(col,-1,-1)):
        if board[i][j]:
            return False
    #left diagonal
    for i,j in zip(range(row,-1,-1), range(col,N)):
        if board[i][j]:
            return False
    return True
        
        
#Returns True if board can be formed with non attaking queens
def nonAttackingQueens(board,row,numberOfQueens):
    #If all queens placed
    if row >= numberOfQueens:
        return True
    
    #Taking one row at a time and moving columnwise
    
    for i in range(numberOfQueens):
        #print("{} {}".format(row,i))
        if isSafe(board,row,i):
            board[row][i] = 1
            if nonAttackingQueens(board,row+1,numberOfQueens):
                #print("one found")
                return True

        board[row][i] = 0
        
    return False

#Fixing position of one queen in first row and then checking if Valid board is possible
def numberOfSolutions(n):
    board = [[0 for col in range(n)] for row in range(n)]
    count = 0
    for i in range(n):
        board[0][i] = 1
        if nonAttackingQueens(board,1,n):
            count +=1
        board = [[0 for col in range(n)] for row in range(n)] 
    return count
    
    
    


# In[181]:


print(numberOfSolutions(4))


# In[ ]:





# In[ ]:




