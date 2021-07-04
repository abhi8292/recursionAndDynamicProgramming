'''
Goal : Find no of set bits for each no in the range 0 to Num and push them individually in an array.

input = num = 5

        Binary  | num
        ______________
         0      | 0
         1      | 1
        ______________
        1 0     | 2
        1 1     | 3
        ______________
        1 0 0   | 4
        1 0 1   | 5


    ans = [0,1,1,2,1,2]


approach 1 : convert each number in binary and conut the number of 1 in binary representation of that number and keep pushing
            in result array

            Time Complexity = O(32 *N)
            where 32 is max number bit can be used for integer representation
approch 2 : if number N is even . then it will be having same number of set bit as N/2
            if number N is odd then it will be having 1 + number of set bit in N/2

            0   => 0 number of bits
            1   => 1/2=> 0 => 1 + 0 number of bits
            2   => 2/1 => 1 => 1 number of bits
            3   => 2/3 => 1 => 1 + 1 number of bits

'''


def countSetBit(nums):
    ans = [0] *(nums+1)

    for i in range(1,nums+1):
        if i %2 == 0:
            ans[i] = ans[i//2]
        else:
            ans[i] = 1 + ans[i//2]
    print(ans)


inp = 16
countSetBit(inp)