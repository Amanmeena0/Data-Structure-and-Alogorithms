from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)
        
        longest = 0

        for x in num:

            if x - 1 not in num:
                length = 1

                while x + length in num:
                    length += 1

                longest = max(longest, length)

        return longest





        return size
    
def main():

    sol = Solution()
    array = list(map(int, input("Enter numbers separated by spaces: ").split()))
    # k = int(input("Enter the number: "))
    print(sol.longestConsecutive(array))
    # sol.sortColors(array)
    # for i in array:
    #     print(i, end=" ")

if __name__ == "__main__":
    main()