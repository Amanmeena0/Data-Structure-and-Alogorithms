from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        



        
def main():

    sol = Solution()
    array = list(map(int, input("Enter numbers separated by spaces: ").split()))
    # k = int(input("Enter the number: "))
    # print(sol.maxProfit(array))
    sol.sortColors(array)
    for i in array:
        print(i, end=" ")

if __name__ == "__main__":
    main()