def main(n):
    if n == 0:
        return 1
    
    result1 = main(n-1)
    result2 = n * result1
    return result2




print(main(5))