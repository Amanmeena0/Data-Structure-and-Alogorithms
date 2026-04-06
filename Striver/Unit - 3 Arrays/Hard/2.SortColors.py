from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        low = 0
        high = len(nums) - 1
        mid = 0


        while(mid <= high):

            if nums[mid] == 2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
                mid+=1
            elif nums[mid] == 0:
                nums[mid], nums[low] = nums[low],nums[mid]
                low+=1
                mid+=1      
            elif nums[mid] == 1:
                mid+=1
                






        
def main():

    sol = Solution()
    array = list(map(int, input("Enter numbers separated by spaces: ").split()))
    k = int(input("Enter the number: "))
    print(sol.longestSubarray(array,k))
    

if __name__ == "__main__":
    main()