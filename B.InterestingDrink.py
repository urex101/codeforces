#706B
import bisect
import sys

input = sys.stdin.read

def solve():

    data = input().split()    
    numberofshops = int(data[0])
    listofshops = [int(x) for x in data[1:numberofshops + 1]]
    listofshops.sort()
    days = int(data[numberofshops + 1])
    budgets = data[numberofshops + 2:]
    
    
    for i in range(days):
        day_budget = int(budgets[i])
        count = bisect.bisect_right(listofshops, day_budget)
        print(count)
solve()
