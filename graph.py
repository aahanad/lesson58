class graph:
    def __init__(self,n):
        self.n=n
        self.adj=[[]*n for i in range (n)]
    def create_edge (self,x,y):
        self.adj[x-1].append(y-1)
        self.adj[y-1].append(x-1)

        print (self.adj)
    def bfs(self,source):
        result=[]
        queue=[]
        visited=[False]*self.n
        visited[source]=True
        queue.append(source)
        while len(queue)>0:
            s=queue.pop(0)

            result.append(s)
            for node in self.adj[s]:
                if visited[node]==False:
                    queue.append(node)
                    visited[node]=True
                print(visited)
                #print (queue)
        return(result)


g1=graph(5)
g1.create_edge(1,3)
g1.create_edge(2,4)
g1.create_edge(3,5)
g1.create_edge(4,1)
g1.create_edge(2,5)
g1.create_edge(3,2)
g1.create_edge(1,2)
print (g1.bfs(3))
