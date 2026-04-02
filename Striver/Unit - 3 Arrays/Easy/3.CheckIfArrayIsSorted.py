from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)
        for i in range(n):

            if nums[i] > nums[(i + 1) % n]:
                count +=1 
            
        return count <= 1


def main():

    sol = Solution()
    array = list(map(int, input("Enter numbers separated by spaces: ").split()))
  
    print(sol.check(array))

if __name__ == "__main__":
    main()

