t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    a %= 10
    if a == 0:
        print(10)
        continue
    # 각 숫자의 일의 자리 주기
    cycles = {
        1: [1],
        2: [2, 4, 8, 6],
        3: [3, 9, 7, 1],
        4: [4, 6],
        5: [5],
        6: [6],
        7: [7, 9, 3, 1],
        8: [8, 4, 2, 6],
        9: [9, 1]
    }
    cycle = cycles[a]
    index = (b - 1) % len(cycle)
    print(cycle[index])
