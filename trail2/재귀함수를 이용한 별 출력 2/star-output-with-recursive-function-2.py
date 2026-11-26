n = int(input())

# Please write your code here.
def f(k):
    if k == 0:
        return
    print("* " * k)
    f(k - 1)
    print("* " * k)


f(n)