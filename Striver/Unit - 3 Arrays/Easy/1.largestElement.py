class Solutuon:
    def largestElement(self,nums, n):
        
        return max(nums)
    
def main():

    sol = Solutuon()
    array = list(map(int, input("Enter numbers separated by spaces: ").split()))
    n = len(array)
    print(sol.largestElement(array, n))

if __name__ == "__main__":
    main()




