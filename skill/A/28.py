import sys
from collections import deque


def solve():
    input_data = sys.stdin.read().split()
    S = int(input_data[0])
    P = int(input_data[1])

    def calc_strength(X, q):
        return X * (100 + q) // 100

    queue = deque()
    queue.append((S, P))
    ans = S
    visited = set()
    visited.add((S, P))
    while queue:
        s, p = queue.popleft()
        if ans < s:
            ans = s
        if p == 0:
            continue
        for i in range(1, p + 1):
            s_new = calc_strength(s, i)
            p_new = p - i
            if (s_new, p_new) not in visited:
                queue.append((s_new, p_new))
                visited.add((s_new, p_new))
    # def dfs(s, p):
    #     if p == 0:
    #         return s
    #     max_strength = s
    #     for i in range(1, s + 1):
    #         S = calc_strength(s, i)
    #         S_tmp = dfs(S, p - i)
    #         max_strength = max(max_strength, S_tmp)
    #
    #     return max_strength

    print(ans)


if __name__ == "__main__":
    solve()
