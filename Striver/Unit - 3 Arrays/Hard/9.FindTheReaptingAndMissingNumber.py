from typing import List
from collections import Counter
class Solution:
    def findMissingRepeatingNumbers(self, nums):
        n = len(nums)
        freq = Counter(nums)
        sorted(freq.items())
        repeating = -1
        missing = -1
    
        for i in range(1, n + 1):

            if freq[i] == 0 :
                missing = i
            elif freq[i] == 2:
                repeating = i
            
        return [repeating, missing]
        
def main():
    sol = Solution()
    array = list(map(int, input("Enter numbers separated by spaces: ").split()))
    # array1 = list(map(int, input("Enter numbers separated by spaces: ").split()))

    print(sol.findMissingRepeatingNumbers(array))

    # for num in array:
    #     print(num)

    
if __name__ == "__main__":
    main()