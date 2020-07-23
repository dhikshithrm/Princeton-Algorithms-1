import weightedqu as wqu
class  PathCompressionWQU(wqu.WeightedUnionFindUF):
    def root(self,p):
        while(p != self.uid[p]):
            self.uid[p] = self.uid[self.uid[p]]
            p = self.uid[p]
        return p
Pc = PathCompressionWQU(10)
for i in range(10):
    print(Pc.root(i))