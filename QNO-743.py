import heapq as hq
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        #CREATING GRAPH
        g = {i:[] for i in range(1,n+1)}
        for u,v,w in times:
            g[u].append((v,w))

        #MIN-HEAP (TIME,NODE)
        h = [(0,k)]
        vis = {}

        while h:
            time,node = hq.heappop(h)
            if node in vis:
                continue
            vis[node] = time

            for nei ,wt in g[node]:
                if nei not in vis:
                    hq.heappush(h, (time + wt, nei))

        #IF ALL NODES VISITED

        if len(vis) == n:
            return max(vis.values())
        return -1

        
        