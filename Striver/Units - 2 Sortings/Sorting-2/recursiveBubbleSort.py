class Solution:
    """
        bubbleSort:
            function:
                bubblesortRecursive: recursive 
                    function to sort array
                __str__: format print of array 
                __init__: constructor
                    function in python 
            variables:
                self.array = contains array 
                self.length= length of array
    """
    def __init__(self,array ):
        self.array = array
        self.length = len(array)

    def __str__(self):
        return " ".join([str(x) for x in self.array])
    
    def BubbleSortRecursive(self, n=None) :


        if n is None:
            n = self.length    
        
        count = 0

        if n == 1:
            return 
        

        for i in range(n-1):
            if self.array[i] > self.array[i + 1]:
                self.array[i], self.array[i + 1] = self.array[i + 1],self.array[i]
                count = count + 1
        if (count == 0):
            return 
        
        self.BubbleSortRecursive(n - 1)

def main():
        

    nums = [7,3,6,4]
    sol = Solution(nums)
    sol.BubbleSortRecursive()

    print("Sorted array :\n", sol)

if __name__ == "__main__":
    main()