def main():
    # Write code here
    for _ in range(int(input())):
        list = input()
        arr = [0] * 26
        for i in list:
            arr[ord(i) - ord('a')] += 1
        maxi = max(arr)
        print(chr(arr.index(maxi) + 97))
    #  print(citizen,maxPerson,safePerson)


main()