class graph:
    def __init__(self,n):
        self.n=n
        self.adj=[[]*n for i in range (n)]
    def create_edge (self,x,y):
        self.adj[x-1].append(y)
        self.adj[y-1].append(x)
        print (self.adj)
g1=graph(5)
g1.create_edge(1,3)
g1.create_edge(2,4)
g1.create_edge(3,5)
g1.create_edge(4,1)
g1.create_edge(2,5)
g1.create_edge(3,2)
g1.create_edge(1,2)