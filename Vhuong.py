n = int(input("Nhập n: "))

for i in range(1, n+1):
    for j in range(1, n+1):
        # Nửa trên (tam giác góc trái trên)
        if i <= n//2+1:
            if j == 1 or i == 1 or j == i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        # Nửa dưới (tam giác góc phải dưới)
        else:
            if j == n or i == n or j == n-i+1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print()
5