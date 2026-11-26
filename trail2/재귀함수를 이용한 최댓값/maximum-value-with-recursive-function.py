def mx(i):
    return arr[0] if i == 0 else max(arr[i], mx(i - 1))


n = int(input())
arr = list(map(int, input().split()))
print(mx(n - 1))