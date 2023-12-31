# -*- coding: utf-8 -*-
"""Prob1.ipynb of SE20UARI052

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kI8WiW2A2ROM3eofELRbgJGUu3nXFqWC
"""

def find_waiting_time(processes, n, bt, wt):
    wt[0] = 0

    for i in range(1, n):
        wt[i] = bt[i - 1] + wt[i - 1]

def find_turnaround_time(processes, n, bt, wt, tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]

def fcfs(processes, n, bt, wt, tat):
    find_waiting_time(processes, n, bt, wt)
    find_turnaround_time(processes, n, bt, wt, tat)

def sjf(processes, n, bt, wt, tat):
    bt_copy = bt.copy()
    bt_copy.sort()

    for i in range(n):
        index = bt.index(bt_copy[i])
        wt[index] = sum(bt[:i])
        find_turnaround_time(processes, n, bt, wt, tat)

def priority_scheduling(processes, n, bt, wt, tat, priority):
    for i in range(n):
        for j in range(n):
            if priority[i] < priority[j]:
                priority[i], priority[j] = priority[j], priority[i]
                processes[i], processes[j] = processes[j], processes[i]
                bt[i], bt[j] = bt[j], bt[i]

    find_waiting_time(processes, n, bt, wt)
    find_turnaround_time(processes, n, bt, wt, tat)

def round_robin(processes, n, bt, wt, tat, quantum):
    remaining_bt = bt.copy()
    time = 0

    while True:
        done = True
        for i in range(n):
            if remaining_bt[i] > 0:
                if remaining_bt[i] > quantum:
                    time += quantum
                    remaining_bt[i] -= quantum
                else:
                    time += remaining_bt[i]
                    wt[i] = time - bt[i]
                    remaining_bt[i] = 0
        if done:
            break

if __name__ == "__main__":
    processes = ["p1", "p2", "p3", "p4"]
    n = len(processes)
    bt = [24, 3, 3, 12]
    wt = [0] * n
    tat = [0] * n
    arrival_time = [0, 4, 5, 6]
    priority = [3, 1, 4, 2]
    quantum = 4

    # FCFS
    fcfs(processes, n, bt, wt, tat)
    avg_waiting_time_fcfs = sum(wt) / n
    avg_turnaround_time_fcfs = sum(tat) / n

    # SJF
    sjf(processes, n, bt, wt, tat)
    avg_waiting_time_sjf = sum(wt) / n
    avg_turnaround_time_sjf = sum(tat) / n

    # Priority Scheduling
    priority_scheduling(processes, n, bt, wt, tat, priority)
    avg_waiting_time_priority = sum(wt) / n
    avg_turnaround_time_priority = sum(tat) / n

    # Round Robin
    round_robin(processes, n, bt, wt, tat, quantum)
    avg_waiting_time_rr = sum(wt) / n
    avg_turnaround_time_rr = sum(tat) / n

    print("FCFS:")
    for i in range(n):
        print(f"{processes[i]}: Waiting Time = {wt[i]}, Turnaround Time = {tat[i]}")

    print(f"Average Waiting Time: {avg_waiting_time_fcfs}")
    print(f"Average Turnaround Time: {avg_turnaround_time_fcfs}\n")

    print("SJF:")
    for i in range(n):
        print(f"{processes[i]}: Waiting Time = {wt[i]}, Turnaround Time = {tat[i]}")

    print(f"Average Waiting Time: {avg_waiting_time_sjf}")
    print(f"Average Turnaround Time: {avg_turnaround_time_sjf}\n")

    print("Priority Scheduling:")
    for i in range(n):
        print(f"{processes[i]}: Waiting Time = {wt[i]}, Turnaround Time = {tat[i]}")

    print(f"Average Waiting Time: {avg_waiting_time_priority}")
    print(f"Average Turnaround Time: {avg_turnaround_time_priority}\n")

    print("Round Robin:")
    for i in range(n):
        print(f"{processes[i]}: Waiting Time = {wt[i]}, Turnaround Time = {tat[i]}")

    print(f"Average Waiting Time: {avg_waiting_time_rr}")
    print(f"Average Turnaround Time: {avg_turnaround_time_rr}\n")

    # Determine the most suitable algorithm
    avg_waiting_times = [avg_waiting_time_fcfs, avg_waiting_time_sjf, avg_waiting_time_priority, avg_waiting_time_rr]
    avg_turnaround_times = [avg_turnaround_time_fcfs, avg_turnaround_time_sjf, avg_turnaround_time_priority, avg_turnaround_time_rr]

    algorithms = ["FCFS", "SJF", "Priority Scheduling", "Round Robin"]
    min_avg_waiting_time = min(avg_waiting_times)
    min_avg_turnaround_time = min(avg_turnaround_times)

    print(f"The most suitable algorithm based on average waiting time is {algorithms[avg_waiting_times.index(min_avg_waiting_time)]}")
    print(f"The most suitable algorithm based on average turnaround time is {algorithms[avg_turnaround_times.index(min_avg_turnaround_time)]}")
