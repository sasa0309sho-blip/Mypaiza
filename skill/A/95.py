import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    A = []
    for i in range(N):
        A.append(int(input_data[1 + i]))

    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    R = [0] * (N - 1)
    for i in range(N - 1):
        g = gcd(A[i + 1], A[i])
        R[i] = [(A[i + 1] / g, A[i] / g)]
    ans = 0
    current_ans = 1
    for i in range(1, len(R)):
        if R[i] == R[i - 1]:
            current_ans += 1
        else:
            ans += current_ans * (current_ans + 1) // 2
            current_ans = 1
    ans += current_ans * (current_ans + 1) // 2
    print(ans)


if __name__ == "__main__":
    solve()
