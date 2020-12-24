import sys

n = int(sys.stdin.readline())
RGB = []
for _ in range(n):
    r, g, b = map(int, sys.stdin.readline().split())
    RGB.append((r, g, b))

r_cost, g_cost, b_cost = [0], [0], [0]

for i in range(0, n):
    r, g, b = RGB[i]
    r_cost.append(r + min(g_cost[i], b_cost[i]))
    g_cost.append(g + min(r_cost[i], b_cost[i]))
    b_cost.append(b + min(r_cost[i], g_cost[i]))

print(min(r_cost[n],g_cost[n],b_cost[n]))
