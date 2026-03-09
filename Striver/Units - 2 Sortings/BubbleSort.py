# def bubble_sort(arr):
#     n = len(arr)

#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 # swap
#                 arr[j], arr[j+1] = arr[j+1], arr[j]

#     return arr

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr


arr = [5, 3, 8, 4, 2]
sorted_arr = bubble_sort(arr)
print(sorted_arr)