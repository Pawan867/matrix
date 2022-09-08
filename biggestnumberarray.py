def largest(arr, n):
    max = arr[0]
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max


arr = [19, 127, 67, 79, 867]
n = len(arr)
solution = largest(arr, n)
print("Largest in given array ", solution)
