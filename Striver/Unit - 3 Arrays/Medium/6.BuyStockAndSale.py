from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        for buy in range(len(prices)):
            for sell in range(len(prices)):
                if prices[buy] < prices[sell]:
                    profit = max(profit, prices[sell] - prices[buy])
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