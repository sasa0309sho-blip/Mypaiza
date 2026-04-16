import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    S = int(input_data[0])
    P = int(input_data[1])

    # dp[i] = ポイントをちょうど i 消費したときの強さの最大値
    # 最初はすべて 0 にしておき、0ポイント消費（初期状態）を S とする
    dp = [0] * (P + 1)
    dp[0] = S

    # i: これまでに消費したポイント
    for i in range(P):
        # もし到達不可能な状態ならスキップ（初期状態の 0 のままなど）
        if dp[i] == 0:
            continue

        # j: 今回新しく消費するポイント
        # i + j が最大 P になるまで回す
        for j in range(1, P - i + 1):
            next_S = dp[i] * (100 + j) // 100

            # i + j ポイント消費したときの最大値を更新できれば上書き
            if next_S > dp[i + j]:
                dp[i + j] = next_S

    # 0 ~ P ポイント消費したすべてのパターンのうち、最大の強さを出力
    print(max(dp))


if __name__ == "__main__":
    solve()
