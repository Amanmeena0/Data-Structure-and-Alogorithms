from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = max(nums)

        curr_max = curr_min = 1

        for n in nums:
            temp_max = curr_max * n
            temp_min = curr_min * n
            curr_max = max(n, temp_max, temp_min)
            curr_min = min(n, temp_max, temp_min)

            res = max(res, curr_max)

        return res
def main():

    sol = Solution()
    array = list(map(int, input("Enter numbers separated by spaces: ").split()))
    # k = int(input("Enter the number: "))
    print(sol.reversePairs(array))
    # sol.sortColors(array)
    # for i in array:
    #     print(i, end=" ")

if __name__ == "__main__":
    main()