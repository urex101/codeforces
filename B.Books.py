#279B
import sys

input = sys.stdin.readline

number_of_books, time = map(int, input().split())
book_times = list(map(int, input().split()))
index = 0
x = 0
k = 0
for end in range(number_of_books):
    x += book_times[end]
    while x > time:
        x -= book_times[index]
        index += 1
    k = max(k, end - index + 1)
print(k)
