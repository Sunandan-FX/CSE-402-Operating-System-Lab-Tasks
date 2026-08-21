# Pre-Emptive SJF Code 
pg = [
    ["P1", 0, 16],
    ["P2", 1, 5],
    ["P3", 2, 6],
    ["P4", 3, 1],
    ["P5", 4, 2]
]

n = len(pg)
interval = 4

remaining = [p[2] for p in pg]
ct = [0] * n
tat = [0] * n
wt = [0] * n
table = 0
comp = 0
flow = []

while comp < n:

    shortest = -1
    min_remaining = float('inf')

    for i in range(n):
        pid, at, bt = pg[i]
        if at <= table and remaining[i] > 0:

            if remaining[i] < min_remaining:
                min_remaining = remaining[i]
                shortest = i

    if shortest == -1:
        table += 1
        continue

    flow.append(pg[shortest][0])
    run_time = min(interval, remaining[shortest])
    remaining[shortest] -= run_time
    table += run_time

    if remaining[shortest] == 0:
        comp += 1
        ct[shortest] = table

        at = pg[shortest][1]
        bt = pg[shortest][2]

        tat[shortest] = ct[shortest] - at
        wt[shortest] = tat[shortest] - bt

results = []

for i in range(n):
    results.append([
        pg[i][0], pg[i][1], pg[i][2], ct[i], tat[i], wt[i]
    ])
results.sort(key=lambda x: int(x[0][1:]))
print("\nPID\tAT\tBT\tCT\tTAT\tWT")
total_tat = 0
total_wt = 0

for process in results:
    pid, at, bt, ct_value, tat_value, wt_value = process

    print(
        pid, "\t", at, "\t", bt, "\t", ct_value, "\t", tat_value, "\t", wt_value
    )

    total_tat += tat_value
    total_wt += wt_value

preemptive_avg_tat = total_tat / n
preemptive_avg_wt = total_wt / n

print("\nAverage TAT =", preemptive_avg_tat)
print("Average WT =", preemptive_avg_wt)
print("The Pre-emptive SJF flow:")
print(" -> ".join(flow), "-> Done")

# Non Pre-Emptive SJF Code
pg = [
    ["P1", 0, 16],
    ["P2", 1, 5],
    ["P3", 2, 6],
    ["P4", 3, 1],
    ["P5", 4, 2]
]

n = len(pg)
table = 0
comp = []
total_tat = 0
total_wt = 0
results = []

while len(comp) < n:
    avil = []

    for process in pg:
        pid, at, bt = process
        if pid not in comp and at <= table:
            avil.append(process)

    if len(avil) == 0:
        table = min(
            p[1]
            for p in pg
            if p[0] not in comp
        )
        continue
        
    avil.sort(key=lambda x: (x[2], x[1]))
    pid, at, bt = avil[0]
    ct = table + bt
    tat = ct - at
    wt = tat - bt
    results.append([
        pid, at, bt, ct, tat, wt
    ])

    total_tat += tat
    total_wt += wt
    table = ct
    comp.append(pid)

execution_order = sorted(results, key=lambda x: x[3])

results.sort(key=lambda x: int(x[0][1:]))
print("\nPID\tAT\tBT\tCT\tTAT\tWT")

for process in results:
    pid, at, bt, ct, tat, wt = process

    print(
        pid, "\t", at, "\t", bt, "\t", ct, "\t", tat, "\t", wt
    )

non_preemptive_avg_tat = total_tat / n
non_preemptive_avg_wt = total_wt / n

print("\nAverage TAT =", non_preemptive_avg_tat)
print("Average WT =", non_preemptive_avg_wt)
print("The Non-Pre-emptive SJF flow:")

for process in execution_order:
    print(process[0], end=" -> ")

print("Done")
print("Pre-emptive SJF VS Non-Pre-emptive SJF:")
print("Operation\t\tAverage TAT\tAverage WT")

print(
    f"Pre-emptive SJF\t\t"
    f"{preemptive_avg_tat:.1f}\t\t"
    f"{preemptive_avg_wt:.1f}"
)

print(
    f"Non-Pre-emptive SJF\t"
    f"{non_preemptive_avg_tat:.1f}\t\t"
    f"{non_preemptive_avg_wt:.1f}"
)
print("\nBest Algorithm:")

if preemptive_avg_tat < non_preemptive_avg_tat and preemptive_avg_wt < non_preemptive_avg_wt:
    print("Pre-emptive SJF is better.")
    print("Reason: It has lower Average TAT and Average WT.")

elif non_preemptive_avg_tat < preemptive_avg_tat and non_preemptive_avg_wt < preemptive_avg_wt:
    print("Non-Pre-emptive SJF is better.")
    print("Reason: It has lower Average TAT and Average WT.")

else:
    print("Both algorithms have similar performance.")
    print("The better algorithm depends on the Average TAT and Average WT.")