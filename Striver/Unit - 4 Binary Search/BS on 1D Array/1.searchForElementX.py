from typing import List



class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        low = 0
        high = len(nums) - 1
        for i in range(len(nums)):

            mid = (low + high) // 2

            if target > nums[mid]:
                low = mid+1
            elif target < nums[mid]:
                high = mid

            else:
                return mid
        return -1


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