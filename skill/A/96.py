import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    train = {}
    L = [0] * N
    R = [0] * N
    for i in range(N):
        L[i] = int(input_data[1 + 2 * i])
        R[i] = int(input_data[2 + 2 * i])
        train[L[i]] = R[i]
    train_sorted_L1 = sorted(train.items(), key=lambda x: x[0])
    train_sorted_R1 = sorted(train_.items(), key=lambda x: x[1])
    for i in range(len(train_sorted_L1)):
        if train_sorted_L1[i] != train_sorted_R1[i]:
            print("No")
            return
    print("Yes")


if __name__ == "__main__":
    solve()
