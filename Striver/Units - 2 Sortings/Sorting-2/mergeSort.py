from typing import List

class Solution:
    def mergeSort(self, nums) :
        if len(nums) <=1:
            return nums

        mid = len(nums)// 2

        leftHalf = nums[:mid]
        rightHalf = nums[mid:]

        sortedLeft = mergeSort(leftHalf)
        sortedRight = mergeSort(rightHalf)

        return merge(sortedLeft, sortedRight)                
    
    def merge(self,left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[j])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result
        
    
sol = Solution()

nums = [7,3,6,4]

result = sol.mergeSort(nums)

print(result)