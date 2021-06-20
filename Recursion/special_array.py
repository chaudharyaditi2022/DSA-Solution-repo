def arraySum(arr, l, depth):
    if l < 0:
        return 0

    if type(arr[l]) is int:
        return arr[l]+ arraySum(arr, l-1, depth)
    elif type(arr[l]) is list:
        tmp = (depth+1) * arraySum(arr[l], len(arr[l])-1, depth+1)
        #print(arraySum(arr[l], len(arr[l])-1, depth+1))
        return  tmp + arraySum(arr,l-1,depth)



arr = [5,2,[7,-1],3,[6,[-13,8],4],[[1,2]]]
print(arraySum(arr,len(arr)-1,1))