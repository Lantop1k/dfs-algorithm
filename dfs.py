# Node points 
nodes=['A','B','S','K','Y','N','Q','H','J','D','X','Z','E','P','T','F',
       'M','L','U','G']


N=len(nodes)  #Number of nodes

graph = []

#A
m=[]
m.append([nodes.index('B'),4])
m.append([nodes.index('N'),4])
graph.append(m)

#B
m=[]
m.append([nodes.index('S'),2])
m.append([nodes.index('Q'),5])
graph.append(m)

#S
m=[]
m.append([nodes.index('K'),2])
m.append([nodes.index('H'),5])
graph.append(m)

#K
m=[]
m.append([nodes.index('Y'),3])
m.append([nodes.index('J'),5])
graph.append(m)


#Y
m=[]
m.append([nodes.index('K'),3])
m.append([nodes.index('D'),3])
graph.append(m)

#N
m=[]
m.append([nodes.index('Q'),5])
m.append([nodes.index('X'),7])
graph.append(m)

#Q
m=[]
m.append([nodes.index('N'),5])
m.append([nodes.index('H'),2])
m.append([nodes.index('Z'),6])
graph.append(m)

#H
m=[]
m.append([nodes.index('Q'),2])
m.append([nodes.index('J'),2])
m.append([nodes.index('E'),2])
graph.append(m)

#J
m=[]
m.append([nodes.index('D'),1])
m.append([nodes.index('P'),8])
m.append([nodes.index('K'),5])
graph.append(m)

#D
m=[]
m.append([nodes.index('T'),1])
graph.append(m)


#X
m=[]
m.append([nodes.index('Z'),8])
m.append([nodes.index('F'),7])
graph.append(m)

#Z
m=[]
m.append([nodes.index('E'),10])
m.append([nodes.index('M'),9])
graph.append(m)

#E
m=[]
m.append([nodes.index('P'),8])
m.append([nodes.index('L'),2])
graph.append(m)

#P
m=[]
m.append([nodes.index('T'),6])
m.append([nodes.index('U'),30])
graph.append(m)

#T
m=[]
m.append([nodes.index('G'),3])
m.append([nodes.index('P'),8])
graph.append(m)


#F
m=[]
m.append([nodes.index('M'),7])
m.append([nodes.index('X'),7])
graph.append(m)

#M
m=[]
m.append([nodes.index('L'),1])
graph.append(m)

#L
m=[]
m.append([nodes.index('U'),2])
graph.append(m)

#U
m=[]
m.append([nodes.index('G'),2])
graph.append(m)

#G
m=[]
m.append([nodes.index('U'),3])
graph.append(m)

graph2=[]
for g in range(len(graph)):
    m=graph[g]

    n=[i[0] for i in m]

    graph2.append(n)

    for i in range(len(m)):
        t=m[i]

        
visitednode = set() # list of nodes to be visited

result=''
#function for the Depth first search algorithm
def dfs(visitednode, graph, newnode):
    global result
    
    if not(newnode in visitednode):  #check if the new node is not in the visted nodes
        
        result+=nodes[newnode]+'-'
        
        visitednode.add(newnode)  # add the new nodes to the visted nodes
        
        for neighbournode in graph[newnode]:  #loop through all the neighbor nodes
            dfs(visitednode, graph, neighbournode) #recursive functions 

# Driver Code
print("Result from the Depth-First Search")
dfs(visitednode,graph2, 0)
print(result[:-1])
