
        n = len(nums)
        for i in range(n):
            for j in range(0, n-i-1):
                
                if  nums[j] < nums[j + 1]:
                    nums[j],nums[j+1] = nums[j],nums[j+1]
        
        return nums


sol = Solution()

nums = [7, 4, 1, 5, 3]

result = sol.selectionSort(nums)

print(result)