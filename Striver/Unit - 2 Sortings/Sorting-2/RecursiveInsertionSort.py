class Solution:
    def InsertionSort(self, arr, i, n):
        if i == n:
            return 
        
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j-1]
            j -= 1
        self.InsertionSort(arr, i + 1, n)
        
# Driver code
Sol = Solution()
arr = [13, 46, 24, 52, 20, 9]
n = len(arr)

print("Before Using Insertion Sort:")
print(arr)

Sol.InsertionSort(arr, 0, n)

print("After Using Insertion Sort:")
print(arr)