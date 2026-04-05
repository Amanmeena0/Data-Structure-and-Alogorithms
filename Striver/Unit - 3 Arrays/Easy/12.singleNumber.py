from typing import List
from collections import Counter

class Solution:

   
    def singleNumber(self, nums: List[int]) -> int:

        freq = Counter(nums)    

        num = 0

        for key in freq:

            number = len(nums)

            if number > nums[key]:
                number = key
                num = nums[key]

        return num
    
        
            
def main():

    sol = Solution()
    array = list(map(int, input("Enter numbers separated by spaces: ").split()))

    print(sol.findMaxConsecutiveOnes(array))
    

if __name__ == "__main__":
    main()