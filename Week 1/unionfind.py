# This is lazy approach
# DATA STRUCTURE
# int uid[n]
# Interpretation: id[i] is parent of i
# Root of i is id[id[id[....id[]...]]]

class UnionFindUF():
    def __init__(self,n,uid=[]):
        self.uid = list(range(n))
    def root(self,p):
        while(self.uid[p]!=p):
            p = self.uid[p]
        return p
    def connected(self,p,q):
        return self.root(p)==self.root(q)
    def union(self,p,q):
        self.uid[self.root(p)] = self.root(q)
UF = UnionFindUF(10)
print(UF.uid)
UF.union(1,2)
print(UF.uid)
