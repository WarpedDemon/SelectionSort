#Internet source / insperation: https://www.programiz.com/dsa/selection-sort

# To sort a[left...right] into ascending order:
# 1. For l = left, ..., right–1, repeat:
# 1.1. Set p such that a[p] is the least of a[l...right].
# 1.2. If p  l, swap a[p] and a[l].
# 2. Terminate.

# Test Vars: a = [4,3,4,5,2,3,4,6,8,9,10]  # O(1)

# Test Vars: 
a = ["fox", "cow", "pig", "cat", "rat", "lion", "tiger", "goat", "dog"]  # O(1)
# Test Vars: a = [23, 56, 7, 44, 768, 90, 107, 22, 45, 66, 99, 1, 12]  # O(1)

arr = a  # O(1)

for l in range(0, len(arr) - 1):  # O(n) - Outer loop runs 'n' times
    # Find the index of the minimum element in the remaining unsorted array
    p = l  # O(n)
    for i in range(l+1, len(arr)):  # O(n^2) - Inner loop runs 'n' times in the worst case
        if arr[i] < arr[p]:  # O(1)
            p = i  # O(1)

    # Swap the found minimum element with the first element
    if p != l:  # O(1)
        arr[p], arr[l] = arr[l], arr[p]  # O(1)

print(arr) # O(1)