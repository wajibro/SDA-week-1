data = [7, 2 ,9 ,1 ,5]
left, right = 0, len(data)-1

while left <= right:
    mid = (left + right)//2
    if data[mid] == 5:
        print('founded')
    elif data[mid] == 5:
        left = mid + 1
    else:
        right = mid -1