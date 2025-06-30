def main(arr,n,l,r):
    # base case
    
    if r < l:
        return -1

    m = (l + r) // 2
    
    if arr[m] == n:
        return m
    
    elif arr[m] > n:
        print("Checking the right")
        main(arr,n,l,m-1)
    elif arr[m] < n:
        print("Checking the left")
        main(arr,n,m+1,r)
    

nums = [1,2,3,4,5,6]
print(main(nums,5,0,len(nums)-1))