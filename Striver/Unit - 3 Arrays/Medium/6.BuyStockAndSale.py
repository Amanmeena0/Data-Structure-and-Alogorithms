from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        Buy = prices[0]
        for i in range(1,len(prices)):
            if prices[i] < Buy:
                Buy = prices[i] 

            profit = max(profit,prices[i] - Buy)
            
        return profit 
        
def main():

    sol = Solution()
    array = list(map(int, input("Enter numbers separated by spaces: ").split()))
    # k = int(input("Enter the number: "))
    print(sol.maxProfit(array))
    # sol.sortColors(array)
    # for i in array:
    #     print(i, end=" ")

if __name__ == "__main__":
    main()