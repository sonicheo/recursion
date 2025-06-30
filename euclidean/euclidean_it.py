def main(a,b):

    while(a % b != 0):
        a,b = b, a % b

    return(b)


print(main(45,10))