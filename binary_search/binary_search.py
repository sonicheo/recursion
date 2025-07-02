def main(arr,n,l,r):
    # base case
    
    if r < l:
        return -1

    m = (l + r) // 2
    if arr[m] == n:
        return m
    
    elif arr[m] > n:
        print("Checking the left")
        return main(arr,n,l,m-1)
    elif arr[m] < n:
        print("Checking the right")
        return main(arr,n,m+1,r)
    

nums = [-5,-4,0,2,4,6,8,100,500]
print(main(nums,500,0,len(nums)-1))