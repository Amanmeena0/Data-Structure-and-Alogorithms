from typing import List

class Solution:
    def longestSubarray(self, nums: List[int], k:int)-> int:
        size = 0

        for i in range(len(nums)):

            sum = 0
            for j in range(i):
                sum += nums[j]
                if sum == k:
                    size = j
                    break

        return size
     
def main():

    sol = Solution()
    array = list(map(int, input("Enter numbers separated by spaces: ").split()))
    k = int(input("Enter the number: "))
    print(sol.longestSubarray(array,k))
    

if __name__ == "__main__":
    main()