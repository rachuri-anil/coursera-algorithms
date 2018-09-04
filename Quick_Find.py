class Quick_Find():
    """docstring for Quick_Find"""
    id = []

    def __init__(self, n=None, arr=None):
        if arr is None:
            self.id = self._construct_array(n)
        else:
            self.id = arr

    def _construct_array(self, n):
        temp = []
        for e in range(n):
            temp.append(e)
        return temp

    def is_Connected(self, p, q):
        return self.id[p] == self.id[q]

    def union(self, p, q):
        pid = self.id[p]
        qid = self.id[q]
        for n in range(len(self.id)):
            if self.id[n] == pid:
                self.id[n] = qid


if __name__ == '__main__':
    test = Quick_Find(5)
    print test.is_Connected(3, 4)
    test.union(3, 4)
    print test.is_Connected(3, 4)
