# This Algorithm Is Just An Improvement Over unionfind
# DISADVANTAGES OF UNION FIND: FOR LONG TREES FIND METHOD WAS TOO EXPENSIVE
# So What We Could Do Do Is Just Try Not To Form Long Trees While Building The Trees Itself
# Implementation: Union Method Should Join ROOT Of The Smaller Tree To The Root Of THe Bigger Tree
# DATA STRUCTURE. Same as quick-union,but maintain extra array sz[i] which keeps track of size of the tree
class WeightedUnionFindUF():
    def __init__(self,n,uid=[],sz=[]):
        self.uid = list(range(n))
        self.sz = [1]*n
    def root(self,p):
        while(self.uid[p]!=p):
            p = self.uid[p]
        return p
    def connected(self,p,q):
        return self.root(p)==self.root(q)
    def union(self,p,q):
        if(self.sz[self.root(p)]<self.sz[self.root(q)]):
            self.uid[self.root(p)] = self.root(q)
            self.sz[p]+=self.sz[q]
        else:
            self.uid[self.root(q)] = self.root(p)
            self.sz[q]+=self.sz[p]

WUF = WeightedUnionFindUF(10)
WUF.union(1,2)
print(WUF.uid)

