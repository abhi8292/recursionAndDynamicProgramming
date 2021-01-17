'''
Program is to find fibonacci of entered number using recursion
'''
def fib(num):
    if num <=2:
        return 1
    else:
        return fib(num-1)+fib(num-2)

print(fib(6))
print(fib(20))
print(fib(30))
print(fib(100))