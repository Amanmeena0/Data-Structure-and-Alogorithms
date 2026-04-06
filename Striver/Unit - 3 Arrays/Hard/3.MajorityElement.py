from typing import List
from collections import Counter

class Solution:
    def sortColors(self, nums: List[int]) -> int:
        
        freq = Counter(nums)
        n = len(nums)
        n /= 2

        for key in freq:
            if freq[key] > n:
                return key

        return 

    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate
    

def main():

    sol = Solution()
    array = list(map(int, input("Enter numbers separated by spaces: ").split()))
    # k = int(input("Enter the number: "))
    print(sol.sortColors(array))
    # sol.sortColors(array)
    # for i in array:
    #     print(i, end=" ")

if __name__ == "__main__":
    main()