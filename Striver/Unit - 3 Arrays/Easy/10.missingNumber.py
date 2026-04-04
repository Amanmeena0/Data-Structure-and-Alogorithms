from typing import List

class Solution:

    #brute force approach 
    def unionArray(self, nums: List[int]) -> int:
        missingNumber = 0
        n = len(nums)
        nums.sort()

        for i in range(n+1):

            if i != nums[i]:
                missingNumber = i

        return missingNumber
            
def main():

    sol = Solution()
    array = list(map(int, input("Enter numbers separated by spaces: ").split()))

    print(sol.unionArray(array))
    

if __name__ == "__main__":
    main()