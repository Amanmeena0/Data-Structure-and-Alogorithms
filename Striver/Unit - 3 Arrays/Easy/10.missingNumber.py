from typing import List

class Solution:

    #brute force approach 
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        for i in range(n):
            if nums[i] != i:
                return i

        return n  # if all indices match
            
def main():

    sol = Solution()
    array = list(map(int, input("Enter numbers separated by spaces: ").split()))

    print(sol.missingNumber(array))
    

if __name__ == "__main__":
    main()


