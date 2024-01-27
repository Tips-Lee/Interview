class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        adjacency = [[] for _ in range(numCourses)]
        # adjacency = [[]] * numCourses
        indegree = [0 for _ in range(numCourses)]
        for j, i in prerequisites:
            adjacency[i].append(j)
            indegree[j] += 1

        q = []
        for idx, dgr in enumerate(indegree):
            if dgr == 0:
                q.append(idx)

        while q:
            course = q.pop(0)
            numCourses -= 1
            for i in adjacency[course]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)

        if numCourses == 0:
            return True
        else:
            return False


s = Solution()
print(s.canFinish(3, [[1, 0], [1, 2], [0, 1]]))