from typing import List

class Solution:
    def fourSum(self, nums: list[int], target:int) -> list[list[int]]:
        ans = []
        nums.sort()
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i -1]:
                return 
            left = i + 1
            left2 = i + 2
            right = n - 1

            while left < right:
                
                sum = nums[i] + nums[left] + nums[left2] + nums[right]

                if sum < target:
                    left2+=1
                    left+=1
                elif sum > target:
                    right-=1
                else:
                    ans.append([nums[i], nums[left1] , nums[left2], nums[right])
                    while nums[left] == nums[left-1] and left < right:

                        left += 1

                    while nums[left2] == nums[left2-1] and left2< right:
                        left2 += 1
         
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