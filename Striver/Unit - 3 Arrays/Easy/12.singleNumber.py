from typing import List
from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        freq = Counter(nums)    
        num = 0
        number = len(nums)

        if number == 1 :
            return nums[0]   
        for key in freq:


            if number > freq[key]:
                number = freq[key]
                num = key

        return num
        
            
def main():

    sol = Solution()
    array = list(map(int, input("Enter numbers separated by spaces: ").split()))

    print(sol.singleNumber(array))
    

if __name__ == "__main__":
    main()