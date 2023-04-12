def newArr(arr, val):
    n = len(arr)
    if n == 0:
        return [val]

    mid = n // 2
    if mid >= n:
        mid = n - 1

    # shift the elements to the right of the midpoint
    for i in range(n-1, mid, -1):
        arr[i] = arr[i-1]

    # insert the new value into the ( midpoint )
    arr[mid] = val

    return arr
#jkjjgh