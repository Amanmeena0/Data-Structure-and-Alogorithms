from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
                
        low = 0
        high = len(nums) -1
        
        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return True

            if nums[low] == nums[mid] and nums[mid] == nums[high]:
                low += 1
                high -= 1
            
            elif nums[low] <= nums[mid]:
                if nums[low] <= target and nums[mid] > target:
                    high = mid -1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target and nums[high] >= target:
                    low = mid + 1
                else:
                    high = mid - 1
            
            return False

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