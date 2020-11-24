class Rectangle():
    def __init__(self,x1,y1,w,h):
        self.x1 =x1
        self.y1=y1
        self.x2 = x1+w
        self.y2 = y1+h

    @classmethod
    def fromCircle(self, x,y,r):
        x = x-r
        y = y-r
        w = 2*r
        h = 2*r
        return Rectangle(x,y,w,h)
        
    def intersect(self, rect):
        r1 = self
        r2 = rect
        if rect.x1 < self.x1:
            r1,r2=r2,r1
        return r1.x1<r2.x2 and r1.x2>r2.x1 and r1.y1<r2.y2 and r1.y2>r2.y1
        
