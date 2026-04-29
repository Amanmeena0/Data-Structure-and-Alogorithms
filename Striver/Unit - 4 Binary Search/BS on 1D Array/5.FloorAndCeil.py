from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        low = 0
        high = len(nums) - 1
        
        while low <= high:

            mid = (low + high) // 2

            if nums[mid] == target:
                return [nums[mid],nums[mid]]
            elif nums[mid] > target:
                high = mid-1
            elif nums[mid] < target:
                low = mid + 1 
        return [nums[high],nums[low]]


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