from typing import List
class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            self.swap(nums, i, j)
        self.reverse(nums, i + 1)

    def nextPermutation(self, nums)->None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = -1
        n = len(nums)
        for i in range(n-2, -1, -1):
            if(nums[i] < nums[i+ 1]):
                pivot = i
                break

        if(pivot == -1): 
            self.reverse(nums,0) 
            return
        
        for i in range(n-1, pivot, -1):
            if(nums[i] > nums[pivot]):
                self.swap(nums, i, pivot)
                break
        
        self.reverse(nums, pivot+1)


    def reverse(self, nums, start):
        i, j = start, len(nums) - 1
        while i < j:
            self.swap(nums, i, j)
            i += 1
            j -= 1

    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        return nums

def main():

    sol = Solution()
    array = list(map(int, input("Enter numbers separated by spaces: ").split()))
    # k = int(input("Enter the number: "))
    # print(sol.maxProfit(array))
    sol.sortColors(array)
    for i in array:
        print(i, end=" ")

if __name__ == "__main__":
    main()