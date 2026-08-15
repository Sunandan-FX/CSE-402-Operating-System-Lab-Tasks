pg = [
    ["P1", 3, 2],
    ["P2", 2, 2],
    ["P3", 1, 1],
    ["P4", 1, 2],
    ["P5", 0, 1],
    ["P6", 4, 3]
]

table = 0
total_tat = 0
total_wt = 0

re = []
remaining = pg.copy()

print("PID\tAT\tBT\tCT\tTAT\tWT")

while remaining:

    
    available = [p for p in remaining if p[1] <= table]

   
    if not available:
        table = min(p[1] for p in remaining)
        available = [p for p in remaining if p[1] <= table]

    
    p = min(available, key=lambda t: t[2])

    pid, at, bt = p

    ct = table + bt
    tat = ct - at
    wt = tat - bt

    total_tat += tat
    total_wt += wt

    re.append([pid, at, bt, ct, tat, wt])

    table = ct
    remaining.remove(p)

n = len(pg)


re.sort(key=lambda x: int(x[0][1:]))

for i in re:
    print(f"{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}\t{i[5]}")

print("\nAverage TAT =", total_tat / n)
print("\nAverage WT =", total_wt / n)

print("\nExecution time SJF:")
for p in sorted(re, key=lambda x: x[3]):
    print(p[0], end="->")

print("END")