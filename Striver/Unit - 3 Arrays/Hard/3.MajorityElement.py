from typing import List
from collections import Counter

class Solution:
    def sortColors(self, nums: List[int]) -> int:
        
        freq = Counter(nums)


        


        return -1

        
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