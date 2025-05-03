# 정렬을 효율적인 sorted()로 변경
seen = set()
words = []
for _ in range(int(input())):
    w = input().strip()
    if w not in seen:
        seen.add(w)
        words.append(w)

# 첫 번째 기준 len(x) = 길이, x = 사전
words = sorted(words, key=lambda x: (len(x), x))

for w in words:
    print(w)