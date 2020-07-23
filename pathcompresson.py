#WE CAN COMPRESS THE HEIGHT OF THE TREE IN ORDER TO MAKE IT FASTER
import unionfind as u
class PathCompress(u.UnionFindUF):
    def __init__(self,n):
        u.UnionFindUF(n).__init__(self)
    def root(self,p):
        while(p != self.uid[p]):
            self.uid[p] = self.uid[self.uid[p]]
            p = self.uid[p]
        return p