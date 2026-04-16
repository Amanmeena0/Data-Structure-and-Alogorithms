from typing import List
class Solution:
    def merge1(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x : x[0])
        
        merged = []

        for interval in intervals:

            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)

            else:

                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        intervals.sort(key=lambda x : x[0])

        prev = intervals[0]

        for interval in intervals[1:]:

            if interval[0] <= prev[1]:
                prev[1] = max(prev[1], interval[1])
            
            else:
                merged.append(prev)
                prev = interval
        merged.append(prev)
        return merged
                   
def main():
    sol = Solution()
    rows = int(input("Enter the number of rows: "))
    array = [[int(x) for x in  input("Enter numbers separated by spaces: ").split()] for _ in range(rows)]
    # k = int(input("Enter the integer: "))
    print(sol.merge(array))

    
if __name__ == "__main__":
    main()
