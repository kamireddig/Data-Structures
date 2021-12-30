# Linear Search in Python
# Getting the input list and search element
n = int(input('Enter the number of elements in the list : '))

arr = []
for i in range(0,n):
    arr.append(input())

x = int(input('Enter the element to be searched : '))

# Actual Logic for Linear Search
for j in range(len(arr)):
    if arr[j] == x:
        x, j
        ind = arr.index(j)
    else:
        -1

print('The element', x, 'is found at index', j)