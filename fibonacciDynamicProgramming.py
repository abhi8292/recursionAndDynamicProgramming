'''
Program is to find fibonacci of entered number using DynamicProgramming
'''

def fib(num , mem={}):
    if num in mem.keys():
        return mem[num]
    if num <=2:
        return 1
    mem[num] = fib(num-1,mem)+fib(num-2,mem)
    return mem[num]

print(fib(5))
print(fib(20))
print(fib(30))
print(fib(100))