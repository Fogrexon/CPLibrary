"""
UnionFind
nは要素数
UnionFind(要素数)

union(x, y)
xとyに関係性があるので結合

roots()でグループ化されている

"""


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [i for i in range(n)]

    def find(self, x):
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if (x == y):
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        # self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r))
                         for r in self.roots())
