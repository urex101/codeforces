#266A
from itertools import groupby

stone_count = int(input())
stone_layout = input()

consecutive_stones = [(key, len(list(group))) for key, group in groupby(stone_layout)]

repited = stone_count - len(consecutive_stones)

print(repited)
