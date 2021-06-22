#!/usr/bin/env python
# coding: utf-8

# In[12]:



def isValid(arr,row,col,digit):
    #Checking row and column validity
    for i in range(0,9):
        if arr[row][i] == digit or arr[i][col] == digit:
            return False
    
    #Checking Subgrid validity
    rowEnd = ((row//3)+1)*3
    colEnd = ((col//3)+1)*3
    for r in range(rowEnd-3, rowEnd):
        for c in range(colEnd-3,colEnd):
            if arr[r][c] == digit:
                return False
    return True



def sudoku(arr, row,col):
    
    if (row == 8 and col == 9):
        #print(arr)
        return True
    if col == 9:
        row +=1
        col = 0
    
    #Cell not empty
    if arr[row][col] > 0:
        return sudoku(arr, row, col + 1)
    
    #If cell is empty
    #Trying to fill every digit
    for digit in range(1,10):
        #Checking if digit placement is valid
        if isValid(arr,row,col,digit):
            arr[row][col] = digit
            if sudoku(arr,row,col+1): return True
        arr[row][col] = 0
    return False
        
    
                    
arr = [ [3, 0, 6, 5, 0, 8, 4, 0, 0], 
         [5, 2, 0, 0, 0, 0, 0, 0, 0], 
         [0, 8, 7, 0, 0, 0, 0, 3, 1], 
         [0, 0, 3, 0, 1, 0, 0, 8, 0], 
         [9, 0, 0, 8, 6, 3, 0, 0, 5], 
         [0, 5, 0, 0, 9, 0, 6, 0, 0], 
         [1, 3, 0, 0, 0, 0, 2, 5, 0], 
         [0, 0, 0, 0, 0, 0, 0, 7, 4], 
         [0, 0, 5, 2, 0, 6, 3, 0, 0] ]

                    
if(sudoku(arr, 0, 0)):
    print(arr)
else:
    print("No solution exists")


# In[ ]:




