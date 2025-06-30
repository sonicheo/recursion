
def main(arr, val, n=0):
    
    if n > len(arr):
        return -1
    
    if arr[n] == val:
        return n

    return main(arr, val, n+1)


print(main([1, 5, -3, 10, 55, 100], 10))