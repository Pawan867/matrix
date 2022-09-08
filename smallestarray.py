arr = [3, 21, 19, 67, 88]

min = arr[0]

for i in range(0, len(arr)):

    if(arr[i] < min):
        min = arr[i]

print("Smallest number in given array: " + str(min))
