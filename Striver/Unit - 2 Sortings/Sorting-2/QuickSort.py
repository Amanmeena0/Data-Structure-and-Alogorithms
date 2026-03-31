class Method:
    def QuickSort(self,nums, low, high):

        if low < high:
            pivotIndex = self.helper(nums, low, high)

            self.QuickSort(nums, low, pivotIndex - 1)

            self.QuickSort(nums, pivotIndex + 1, high)

    def helper(self,arr, low, high):


        pivot = arr[high]

        i = low - 1

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1

                arr[i], arr[j] = arr[j],arr[i]

        arr[i + 1] , arr[high] = arr[high], arr[i +1 ]
        return  i + 1
    


nums = [3,5,3,2,7,5,3]

n = len(nums)
sort = Method()
sort.QuickSort(nums,0,  n - 1)


print(*nums)
