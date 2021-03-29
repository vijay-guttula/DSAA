

from collections import namedtuple

Job = namedtuple("Job", ["assigned_to", "started_at", "done_at"])


def Construct(n, tasks):
    work_flow = []
    w = 0
    for i in range(len(tasks)):
        if i < n:
            work_flow.append(Job(w, 0, tasks[i]))
            w += 1
            if w >= n:
                w = 0
            continue
        work_flow.append(
            Job(w, work_flow[i - n].done_at, work_flow[i - n].done_at + tasks[i]))
        w += 1
        if w >= n:
            w = 0

    return work_flow


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    data = list(map(int, input().split()))

    work_flow = Construct(n, data)

    for work in work_flow:
        print(work.assigned_to, work.started_at)
