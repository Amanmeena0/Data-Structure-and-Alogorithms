from typing import List
from collections import Counter
class Solution:
    
    #brute force code
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
    
    #optimized code 
    def singleNumber1(self, nums: List[int]) -> int:
        freq = Counter(nums)

        for key in freq:
            if freq[key] == 1:
                return key
    

    #Best approach for this xor approach
    def singleNumber1(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num

        return result


def main():

    sol = Solution()
    array = list(map(int, input("Enter numbers separated by spaces: ").split()))

    print(sol.singleNumber(array))
    

if __name__ == "__main__":
    main()