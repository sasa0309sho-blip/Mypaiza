import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    A = int(input_data[1])
    B = int(input_data[2])
    # dpはTrueなら到達可能
    dp = [False] * (N + 1)
    dp[0] = True
    for i in range(N):
        if dp[i]:
            if i + A <= N:
                dp[i + A] = True
            if i + B <= N:
                dp[i + B] = True
    for i in range(N):
        if dp[i]:
            remain = N - i
            if remain < A and remain < B:
                dp[N] = True

    ans = 0
    for i in range(1, N + 1):
        if not dp[i]:
            ans += 1
    print(ans)


if __name__ == "__main__":
    solve()
