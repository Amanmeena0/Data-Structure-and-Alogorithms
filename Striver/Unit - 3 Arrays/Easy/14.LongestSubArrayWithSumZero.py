from typing import List

class Solution:
    def longestSubarray(self, nums: List[int])-> int:
        
        size = 0
        for i in range(len(nums)):
            sum = 0

            for j in range(i, len(nums)):
                sum += nums[j]

                if sum == 0:
                    size = max(size, j - i + 1)
                    
        return size
     
def main():

    sol = Solution()
    array = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print(sol.longestSubarray(array))
    

if __name__ == "__main__":
    main()