pg = [
    ["P0", 0, 4],
    ["P1", 1, 3],
    ["P2", 2, 1],
    ["P3", 3, 5],
   
]

time_quantum = 2

n = len(pg)

remaining = [pg[i][2] for i in range(n)]
completion = [0] * n
turnaround = [0] * n
waiting = [0] * n

queue = []
visited = [False] * n

time = 0
completed = 0


flow = []

print("Gantt Chart:")

while completed < n:


    for i in range(n):
        if pg[i][1] <= time and not visited[i]:
            queue.append(i)
            visited[i] = True


    if not queue:
        time += 1
        continue

   
    i = queue.pop(0)


    flow.append(pg[i][0])

    start = time

   
    run_time = min(time_quantum, remaining[i])

    time += run_time
    remaining[i] -= run_time

    print(pg[i][0], ":", start, "->", time)

    
    for j in range(n):
        if pg[j][1] <= time and not visited[j]:
            queue.append(j)
            visited[j] = True

    
    if remaining[i] > 0:
        queue.append(i)

   
    else:
        completion[i] = time
        completed += 1


# Display Round Robin flow
print("\nRound Robin Flow:")
print(" -> ".join(flow))


# Calculate TAT and WT
for i in range(n):
    turnaround[i] = completion[i] - pg[i][1]
    waiting[i] = turnaround[i] - pg[i][2]


print("Round Robin Serial: ")
print("\nProcess\tAT\tBT\tCT\tTAT\tWT")

total_tat = 0
total_wt = 0

for i in range(n):
    print(
        pg[i][0], "\t",
        pg[i][1], "\t",
        pg[i][2], "\t",
        completion[i], "\t",
        turnaround[i], "\t",
        waiting[i]
    )

    total_tat += turnaround[i]
    total_wt += waiting[i]


print("\nAverage Turnaround Time =", total_tat / n)
print("Average Waiting Time =", total_wt / n)

print(" / // ")
print("For FCFS: ")

pg.sort(key=lambda t: t[1])

table = 0
t_tat = 0
t_wt = 0

re = []

print("PID\tAT\tBT\tCT\tTAT\tWT")


for p in pg:
    pid,at,bt = p
    if table < at:
       table = at

    ct = table + bt
    tat = ct - at
    wt = tat - bt

    t_tat += tat
    t_wt += wt

    

    re.append([pid, at, bt, ct, tat, wt])
    table = ct

n = len(pg)

re.sort(key=lambda x: int(x[0][1:]))
for i in re:
    print(f"{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}\t{i[5]}")

print("FCFS Serial: ")
for i in pg:
    print(i[0], end = "-> ")

print("End")

print("\nAverage TAT=",t_tat/n)
print("\nAverage WT=",t_wt/n)

print("FCFS VS RoundRobin: \n")
print(f"{"Algo"}\t\t{"Average Turnaround Time"}\t\t{"Average Waiting Time"}")
print(f"{"Round_Robin"}\t\t{total_tat/n}\t\t\t\t{total_wt/n}")
print(f"{"FCFS"}\t\t\t{t_tat/n}\t\t\t\t{t_wt/n}")