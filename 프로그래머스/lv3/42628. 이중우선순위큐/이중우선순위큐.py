import heapq

def solution(operations):
    heap = []
    for o in operations:
        if o.startswith("D"):
            if not heap:
                continue
            if o.startswith("D 1"):
                heap.remove(heapq.nlargest(1, heap)[0])
            else:
                heapq.heappop(heap)
        else:
            heapq.heappush(heap, int(o[1:]))


    return [heapq.nlargest(1, heap)[0], heap[0]] if heap else [0, 0]