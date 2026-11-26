N = int(input())

# Please write your code here.
def f(n):
    if n:
        print(n, end=" ")
        f(n - 1)
        print(n, end=" ")


f(N)