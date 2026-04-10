from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        
        longest = 0

        for x in num_set:

            if x - 1 not in num_set:

                length = 1

                while x + length in num_set:
                    
                    length += 1

                longest = max(longest, length)

        return longest





        return size
    
def main():

    sol = Solution()
    array = list(map(int, input("Enter num_setbers separated by spaces: ").split()))
    # k = int(input("Enter the num_setber: "))
    print(sol.longestConsecutive(array))
    # sol.sortColors(array)
    # for i in array:
    #     print(i, end=" ")

if __name__ == "__main__":
    main()