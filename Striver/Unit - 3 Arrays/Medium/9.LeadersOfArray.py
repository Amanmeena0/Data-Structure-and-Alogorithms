from typing import List

class Solution:
    def leaders(self, nums: List[int]) -> List:
        
        ans = []
        n = len(nums)
        number = float('-inf')
        for i in range(n-1,-1, -1):
            
            if nums[i] > number:
                number = nums[i]
                ans.append(number)        

       
        return ans[::-1]
    
def main():

    sol = Solution()
    array = list(map(int, input("Enter numbers separated by spaces: ").split()))
    # k = int(input("Enter the number: "))
    print(sol.leaders(array))
    # sol.sortColors(array)
    # for i in array:
    #     print(i, end=" ")

if __name__ == "__main__":
    main()