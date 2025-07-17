class Solution(object):
    def minimumEffortPath(self, heights):
        rows, cols = len(heights), len(heights[0])
        distance = [[float('inf')] * cols for _ in range(rows)]
        distance[0][0] = 0

        min_heap = [(0, 0, 0)]  # (effort, row, col)
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        while min_heap:
            effort, r, c = heapq.heappop(min_heap)

            if r == rows - 1 and c == cols - 1:
                return effort

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    curr_diff = abs(heights[r][c] - heights[nr][nc])
                    new_effort = max(effort, curr_diff)

                    if new_effort < distance[nr][nc]:
                        distance[nr][nc] = new_effort
                        heapq.heappush(min_heap, (new_effort, nr, nc))