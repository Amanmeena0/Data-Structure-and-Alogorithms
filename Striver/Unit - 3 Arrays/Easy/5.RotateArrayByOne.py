from typing import List

class Solution:
    def Solve(self, nums: List[int]) -> bool:
        
        n = len(nums)

        if n == 0:
            return 
        
        temp = [0]*n

        for i in range(1,n):

            temp[i - 1] = nums[i]

        temp[n - 1]  =  nums[0]

        for num in temp:
            print(num, end=" ")

        print()

def main():

    sol = Solution()
    array = list(map(int, input("Enter numbers separated by spaces: ").split()))
  
    sol.Solve(array)

if __name__ == "__main__":
    main()
