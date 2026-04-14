from typing import List

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        nums.sort()
        n = len(nums)
    
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1    

            while right > left:

                sum = nums[i]  + nums[left] + nums[right]
            
                if sum < 0:
                    left +=1 
                elif sum > 0:
                    right -= 1

                else:

                    ans.append([nums[i], nums[left], nums[right]])

                    left += 1

                    while nums[left] == nums[left- 1] and left < right:
                        left += 1
        return ans




def main():

    sol = Solution()
    array = list(map(int, input("Enter numbers separated by spaces: ").split()))
    # k = int(input("Enter the number: "))
    print(sol.threeSum(array))
    # sol.sortColors(array)
    # for i in array:
    #     print(i, end=" ")

if __name__ == "__main__":
    main()