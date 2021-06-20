def permutations(arr,start, end):
    if start ==  end:
        print(arr)
        
    for i in range(start,end+1):
        arr[start],arr[i] = arr[i],arr[start] #swap
        permutations(arr,start+1,end)
        arr[start],arr[i] = arr[i],arr[start] #To undo change in original array -> backtrack
        
    
a=[1,2,3]    
permutations(a,0, len(a)-1)      