def bubbleSort(arr):
    p = 0
    count = 0
    flag = True
    while flag:
        for i in range(1,len(arr)-count):
            if arr[p] > arr[i]:
                temp = arr[p]
                arr[p] = arr[i]
                arr[i] = temp
                p = i

        print(arr)

li = [6,5,9,1,10,2]

bubbleSort(li)