import time

data = [1,2,7,5,9]
# left, right = 0, len(data)-1

# while left <= right:
#     mid = (left + right)//2
#     print(left, right, mid)
#     if data[mid] == 5:
#         print('founded')
#     elif data[mid] < 5:
#         left = mid + 1
#     else:
#         right = mid - 1
#     time.sleep(1)

def binarySearch(arr, targetVal):
  left = 0
  right = len(arr) - 1

  while left <= right:
    mid = (left + right) // 2

    if arr[mid] == targetVal:
      return mid

    if arr[mid] < targetVal:
      left = mid + 1
    else:
      right = mid - 1

  return -1

mylist = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
x = 5

result = binarySearch(data, x)

if result != -1:
  print("Found at index", result)
else:
  print("Not found")