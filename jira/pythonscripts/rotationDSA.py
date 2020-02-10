def rverseArray(arr, start, end):
    while (start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end = end-1

# Function to left rotate arr[] of size n by d
def leftRotate(arr, d):
    n = len(arr)
    #n=7
    rverseArray(arr, 0, d-1)
    #0,1
    rverseArray(arr, d, n-1)
    #2,6
    rverseArray(arr, 0, n-1)
    #0,6

# Function to print an array
def printArray(arr):
    for i in range(0, len(arr)):
        print(arr[i],end=' ')

# Driver function to test above functions
arr = [1, 2, 3, 4, 5, 6, 7,8,9]
leftRotate(arr, 6) # Rotate array by 2
printArray(arr)
