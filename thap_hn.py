def Try(n, A, B, C):
    if (n==1):
        print(A, "->", C )
        return
    Try(n-1, A, C, B)
    Try(1, A, B, C)
    Try(n-1, B, A, C)

n = int(input())
Try(n, 'A', 'B', 'C')