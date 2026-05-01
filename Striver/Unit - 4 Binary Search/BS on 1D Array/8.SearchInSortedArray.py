from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        low= 0
        high = len(nums) -1
        
        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[low]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            
        
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