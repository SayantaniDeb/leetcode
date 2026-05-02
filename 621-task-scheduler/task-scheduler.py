from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq=Counter(tasks)
        pq=[]
        for key,val in freq.items():
            pq.append(-val)
        heapq.heapify(pq)
        time=0
        q=deque()
        while pq or q:
            time+=1
            if pq:
                count=1+heapq.heappop(pq)
                if count:
                    q.append([count,time+n])
            if q and q[0][1]==time:
                heapq.heappush(pq,q.popleft()[0])
        return time








        