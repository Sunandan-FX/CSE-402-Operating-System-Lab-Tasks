pg = [
    ["P1",3,2],
    ["P2",2,2],
    ["P3",1,1],
    ["P4",1,2],
    ["P5",0,1],
    ["p6",4,3]
]

pg.sort(key=lambda t: t[1])

table = 0
total_tat = 0
total_wt = 0

re = []

print("PID\tAT\tBT\tCT\tTAT\tWT")


for p in pg:
    pid,at,bt = p
    if table < at:
       table = at

    ct = table + bt
    tat = ct - at
    wt = tat - bt

    total_tat += tat
    total_wt += wt

    

    re.append([pid, at, bt, ct, tat, wt])
    table = ct

n = len(pg)

re.sort(key=lambda x: int(x[0][1:]))
for i in re:
    print(f"{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}\t{i[5]}")

print("\nAverage TAT=",total_tat/n)
print("\nAverage WT=",total_wt/n)


print("\nExcution time FCFS: ")
for p in pg:

 print(p[0],end="->")

print("END")