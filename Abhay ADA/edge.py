class group:
    def __init__(self):
        self.edge=[]
        self.verticle=set()
        
    def add_edge(self,u,v):
        self.edge.append((u,v))
        self.verticle.add(u)
        self.verticle.add(v)
        
    def find(self,parent,i):
        if parent[i]==i:
            return i
        return self.find(parent,parent[i])
    
    def union(self,parent,rank,x,y):
        if rank[x]<rank[y]:
            parent[x]=y
        elif rank[x]>rank[y]:
            parent[y]=x
        else:
            parent[y]=x
            rank[x]+=1 
 