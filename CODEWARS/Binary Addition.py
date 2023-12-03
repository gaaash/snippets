def add_binary(a,b):
    binnum = ''
    num = a + b
    while(num//2 != 0):
        binnum += str(num%2)
        num= num//2

    binnum += str(num % 2)
    return binnum[::-1]