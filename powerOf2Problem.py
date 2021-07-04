

def findPowerOf2Problem(num):
    for i in range(1,num+1):
        print(i,' => ',bin(i),"  " ,i-1," =>",bin(i-1),' ========> ', bin(i&i-1))
    pass


inp = 10253242424
findPowerOf2Problem(inp)