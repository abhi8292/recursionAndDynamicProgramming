'''
Program is to find factorial of the number entered by the user
'''

def fact(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return num *fact(num-1)


if __name__ == '__main__':
    print(fact(996))