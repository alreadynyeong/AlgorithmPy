import heapq

def solution(jobs):
    answer, now, cnt = 0, 0, 0
    heap = []
    last = -1

    while cnt < len(jobs):
        for job in jobs:
            if last < job[0] <= now:
                answer += (now - job[0])
                heapq.heappush(heap, job[1])

        if heap:
            answer += (len(heap) * heap[0])
            last = now
            now += heapq.heappop(heap)
            cnt += 1
        else:
            now += 1

    return answer // len(jobs)