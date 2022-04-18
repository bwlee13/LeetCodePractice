"""
There is series of integer pairs like (1,3),(7,10),(5,7),(4,1). Create unique grouping if any value in pair
matches with any value of other pairs. So for above example output become: (1,3,4) and (7,10,5).
"""
import collections

pairs = [(1,3),(7,10),(5,7),(4,1)]


class UF:
    def __init__(self, N):
        self.parents = list(range(N))

    def union(self, child, parent):
        self.parents[self.find(child)] = self.find(parent)

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]


class Solution:
    def accountsMerge(self, accounts):
        uf = UF(len(accounts))

        ownership = {}
        for ind, val in enumerate(accounts):
            for v in val:
                if v in ownership:
                    uf.union(ind, ownership[v])
                ownership[v] = ind

        ans = collections.defaultdict(list)
        for x, y in ownership.items():
            ans[uf.find(y)].append(x)
        return [sorted(y) for i, y in ans.items()]


s = Solution()
a = s.accountsMerge(pairs)
print(a)