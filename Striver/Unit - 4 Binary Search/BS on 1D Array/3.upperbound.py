from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        low = 0
        high = len(nums) - 1
        ans = 0
        while low <= high:

            mid = (low + high) // 2

            if nums[mid] <= target:
                low = mid + 1
            elif nums[mid] > target:
                ans = mid
                high = mid-1
            

        return ans


def main():

    sol = Solution()
    array = list(map(int, input("Enter numbers separated by spaces: ").split()))
    k = int(input("Enter the number: "))
    print(sol.search(array,k))
    # sol.sortColors(array)
    # for i in array:
    #     print(i, end=" ")

if __name__ == "__main__":
    main()