# Prob-1-of-Process-Scheduling-Analysis

# Problem Statement 

Given the following processes with their arrival times and burst times, schedule the processes using FCFS, SJF, PS, and R (with a time quantum of 4 units) algorithms. After scheduling, determine the waiting time and turnaround time for each process in each scheduling algorithm. Finally, analyze which algorithm is the most suitable based on the average waiting time and average turnaround time.


Processes:
- P1
- P2
- P3
- P4

Arrival Times:
- P1: 0
- P2: 4
- P3: 5
- P4: 6

Burst Times:
- P1: 24
- P2: 3
- P3: 3
- P4: 12

Priorities:
- P1: 3
- P2: 1
- P3: 4
- P4: 2

## FCFS (First-Come, First-Served) Scheduling

| Process | Arrival Time | Burst Time | Completion Time | Turnaround Time | Waiting Time |
| ------- | ------------ | ---------- | --------------- | ---------------- | ------------ |
| P1      | 0            | 24         | 24              | 24               | 0            |
| P2      | 4            | 3          | 27              | 23               | 20           |
| P3      | 5            | 3          | 30              | 25               | 20           |
| P4      | 6            | 12         | 42              | 36               | 30           |

Average Waiting Time: 17.5
Average Turnaround Time: 27

## SJF (Shortest Job First) Scheduling

| Process | Arrival Time | Burst Time | Completion Time | Turnaround Time | Waiting Time |
| ------- | ------------ | ---------- | --------------- | ---------------- | ------------ |
| P1      | 0            | 24         | 24              | 24               | 0            |
| P2      | 4            | 3          | 27              | 23               | 20           |
| P3      | 5            | 3          | 30              | 25               | 20           |
| P4      | 6            | 12         | 42              | 36               | 30           |

Average Waiting Time: 17.5
Average Turnaround Time: 27

## PS (Priority Scheduling) 

| Process | Arrival Time | Burst Time | Priority | Completion Time | Turnaround Time | Waiting Time |
| ------- | ------------ | ---------- | -------- | --------------- | ---------------- | ------------ |
| P2      | 4            | 3          | 1        | 7               | 3                | 0            |
| P4      | 6            | 12         | 2        | 19              | 13               | 1            |
| P1      | 0            | 24         | 3        | 43              | 43               | 19           |
| P3      | 5            | 3          | 4        | 46              | 41               | 36           |

Average Waiting Time: 14
Average Turnaround Time: 25

## RR (Round Robin) Scheduling with Time Quantum of 4 units

| Time  | Process | Burst Remaining |
| ----- | ------- | ---------------- |
| 0     | P1      | 20               |
| 4     | P2      | 0                |
| 8     | P3      | 0                |
| 12    | P4      | 8                |
| 16    | P1      | 16               |
| 20    | P3      | 4                |
| 24    | P4      | 4                |
| 28    | P1      | 12               |
| 32    | P4      | 0                |
| 36    | P3      | 0                |
| 40    | P1      | 8                |
| 44    | P4      | 0                |
| 46    | P1      | 4                |

| Process | Arrival Time | Burst Time | Completion Time | Turnaround Time | Waiting Time |
| ------- | ------------ | ---------- | --------------- | ---------------- | ------------ |
| P1      | 0            | 24         | 46              | 46               | 22           |
| P2      | 4            | 3          | 4               | 0                | 0            |
| P3      | 5            | 3          | 36              | 31               | 26           |
| P4      | 6            | 12         | 44              | 38               | 26           |

Average Waiting Time: 18.5
Average Turnaround Time: 28.75

Based on the average waiting time and average turnaround time, the most suitable scheduling algorithm for this set of processes is Priority Scheduling (PS), as it has the lowest average waiting time (14) and a reasonably low average turnaround time (25).
