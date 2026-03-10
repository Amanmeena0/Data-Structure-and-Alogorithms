class Solution:
    def selectionSort(self, nums):
        for i in range(1, len(nums)):
            key = nums[i]
            j = i - 1

            while j >= 0 and key < nums[j]:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = key
        return nums

sol = Solution()

nums = [7,3,6,4]

result = sol.selectionSort(nums)

print(result)