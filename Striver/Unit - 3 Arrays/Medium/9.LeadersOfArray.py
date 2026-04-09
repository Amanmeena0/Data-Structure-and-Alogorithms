from typing import List

class Solution:
    def leaders(self, nums: List[int]) -> List:
        
        ans = []
        n = len(nums)
        number = nums[n-1]
        for i in range(n-2,-1, -1):
            
            if nums[i] > number:
                number = nums[i]
                ans.append(number)  
            else:
                
            
            
            
        

        return ans
    
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