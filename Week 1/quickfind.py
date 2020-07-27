''' This is eager approach
    DATA STRUCTURE
    uid[n]
    Implementation: p and q are connected iff uid[p] is equal to uid[q]'''

class QuickFindQF():
    def __init__(self,n,uid=[]):
        self.uid = list(range(n))
    def connected(self,p,q):
        return self.uid[p] == self.uid[q]
    def union(self,p,q):
        pid = self.uid[p]
        qid = self.uid[q]
        for i in self.uid:
            if self.uid[i] == pid:
                self.uid[i] = qid
QF = QuickFindQF(10)
QF.union(1,2)
print(QF.uid)
