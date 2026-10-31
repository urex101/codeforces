n, k = map(int, input().split())
ig = list(map(int, input().split()))
target_score = ig[k - 1]

count = 0

for score in ig:
    if score > 0 and score >= target_score:
        count += 1

print(count)