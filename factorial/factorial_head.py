

def main(n):
    if n == 0:
        return 1
    
    return n * main(n-1)



print(main(5))