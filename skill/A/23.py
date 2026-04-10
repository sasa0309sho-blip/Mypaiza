import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    d = [int(x) for x in input_data[1 : N + 1]]
    dp = [False] * (N - 6)
    for i in range(N - 6):
        window = d[i : i + 7]
        if sum(window) <= 5:
            dp[i] = True
    max_ans = 0
    ans = 0
    for i in dp:
        if i:
            ans += 1
            if max_ans < ans:
                max_ans = ans
        else:
            ans = 0
    if max_ans == 0:
        print(max_ans)
    else:
        print(max_ans + 6)


if __name__ == "__main__":
    solve()
