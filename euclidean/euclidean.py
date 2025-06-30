def main(b,s):
    if b % s == 0:
        return s
    
    return main(s,b % s)
    
    
print(main(24,9))