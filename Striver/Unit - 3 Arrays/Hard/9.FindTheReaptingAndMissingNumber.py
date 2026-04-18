from typing import List
from collections import Counter
class Solution:

    # for the 1D array - hash approach
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
    
    # For the 2D array - hash approach
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        
        n = len(grid)
        freq = {}
        
        for row in grid:

            for num in row:
                freq[num] = freq.get(num, 0) + 1
            
        for num in range(1, n*n + 1):
            if num not in freq:
                missing = num 
            elif freq[num] == 2:

                repeat = num
        return [repeat, missing]
    
    #For the 2D array using the maths 
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        n = len(grid)
        total = n * n

        sum_val = sum(num for row in grid for num in row)
        sqr_sum = sum(num*num for row in grid for num in row)

        sum_diff = sum_val - total * (total +1 )// 2
        sqr_diff = sqr_sum - total *(total + 1) * (2 * total + 1)//6


        repeat = (sqr_diff // sum_diff + sum_diff) // 2
        missing = (sqr_diff // sum_diff - -sum_diff) // 2

        return [repeat, missing]


def main():
    sol = Solution()
    array = list(map(int, input("Enter numbers separated by spaces: ").split()))
    # array1 = list(map(int, input("Enter numbers separated by spaces: ").split()))

    print(sol.findMissingRepeatingNumbers(array))

    # for num in array:
    #     print(num)

    
if __name__ == "__main__":
    main()