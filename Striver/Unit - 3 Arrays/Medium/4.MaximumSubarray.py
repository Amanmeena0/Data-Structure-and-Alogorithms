from typing import List
from collections import Counter

class Solution:
    #Brute Force approach - Two Pointer
    def maxSubArray(self, nums):
        ans = float('-inf')
        for i in range(len(nums)):
            cur_sum = 0
            for j in range(i, len(nums)):
                cur_sum += nums[j]
                ans = max(ans, cur_sum)
        return ans

    #Brute Force - Recursive Approach
    def maxSubArray(self, nums):
        def solve(i, must_pick):
            if i >= len(nums): return 0 if must_pick else float('-inf')
            return max(nums[i] + solve(i+1, True), 0 if must_pick else solve(i+1, False))
        return solve(0, False)

    # Approch optimized for solving this question 
    def maxSubArray(self, nums: List[int]) -> int:
        FinaLSum = float('-inf')
        sum = 0
        for num in nums:  
            sum += num
            if FinaLSum < sum:
                FinaLSum = sum
            if sum < 0:
                sum = 0     
        return FinaLSum

def main():

    sol = Solution()
    array = list(map(int, input("Enter numbers separated by spaces: ").split()))
    # k = int(input("Enter the number: "))
    print(sol.maxSubArray(array))
    # sol.sortColors(array)
    # for i in array:
    #     print(i, end=" ")

if __name__ == "__main__":
    main()