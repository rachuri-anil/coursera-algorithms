"""Lazy Approach """


class Weighted_Quick_Union():
    """docstring for Quick_Union"""
    id = []
    sz = []

    def __init__(self, n=None, arr=None):
        if arr is None:
            self.id = self._construct_array(n)
            self.sz = [1] * n
        else:
            self.id = arr
            self.sz = [1] * n

    def _construct_array(self, n):
        temp = []
        for e in range(n):
            temp.append(e)
        return temp

    def root(self, i):
        while(i != self.id[i]):
            i = self.id[i]
        return i

    def is_connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        rootp = self.root(p)
        rootq = self.root(q)
        if rootp == rootq:
            return
        if self.sz[rootp] < self.sz[rootq]:
            self.id[rootp] = rootq
            self.sz[rootq] += self.sz[rootp]
        else:
            self.id[rootq] = rootp
            self.sz[rootp] += self.sz[rootq]


if __name__ == '__main__':
    test = Weighted_Quick_Union(5)
    print test.is_connected(3, 4)
    test.union(3, 4)
    print test.is_connected(3, 4)
