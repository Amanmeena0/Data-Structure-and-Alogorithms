from typing import List

class Solution:
    def fourSum(self, nums: list[int], target:int) -> list[list[int]]:
        ans = []
        nums.sort()
        n = len(nums)

        for i in range(n):

            if i > 0 and nums[i] == nums[i - 1]:
                return 
            
            for j in range(i + 1, n):
                23
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue

                left = j + 1
                right = n - 1

                while left < right:
                    
                    sum = nums[i] + nums[j] + nums[left] + nums[right]

                    if sum < target:
                        
                        left+=1
                    elif sum > target:
                        right-=1
                    else:
                        ans.append([nums[i], nums[j] , nums[left], nums[right]])

                        left += 1
                        right -= 1

                        while nums[left] == nums[left-1] and left < right:
                            left += 1
                        while nums[right] == nums[right+1] and left  <right:
                            right -=1
        return ans

def main():

    sol = Solution()
    array = list(map(int, input("Enter numbers separated by spaces: ").split()))
    k = int(input("Enter the number: "))
    print(sol.fourSum(array, k))
    # sol.sortColors(array)
    # for i in array:
    #     print(i, end=" ")

if __name__ == "__main__":
    main()