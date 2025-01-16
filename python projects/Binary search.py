# Binary search algorithm
def binary_search(arr, target):
    str = 0
    n = len(arr)
    end = n - 1
    while str <= end:
        mid = (str + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            str = mid + 1
        else:
            end = mid - 1
    return -1

#Take input from user for array and target
arr = list(map(int, input("Enter space separated integers: ").split()))

# Ask for index value to search
target = int(input("Enter the value to search: "))

result = binary_search(arr, target)

# Print the result valid or not
if result != -1:
    print(f"Element {target} is found in index {result}.")
else:
    print(f"Element {target} is not found in array ")
