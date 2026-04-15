t = int(input())
for _ in range(t):
    N = int(input())
    if N == 2:
        print("01")

    print("0" + "1"* (N - 2)+"0") 
    