#WE CAN COMPRESS THE HEIGHT OF THE TREE IN ORDER TO MAKE IT FASTER
import unionfind as u
class PathCompress(u.UnionFindUF):
    def root(self,p):
        while(p != self.uid[p]):
            self.uid[p] = self.uid[self.uid[p]]
            p = self.uid[p]
        return p
p = PathCompress(100)

for i in range(100):
    print(p.root(i))