
# only use dictionary and set to save memory and speed up conputation
#read graph into a dictionary
def readData(file):
    # return both graph and reversed graph
    graph = dict()
    graph_rev = dict()
    with open(file) as f:
        for line in f:
            line = line.strip().split()
            if line:
                head, tail = [int(i) for i in line]
                nodes = graph.get(head,set())
                nodes.add(tail)
                graph[head] = nodes

                nodes_rev = graph_rev.get(tail, set())
                nodes_rev.add(head)
                graph_rev[tail] = nodes_rev
    return graph, graph_rev



def DFS(graph):
    finishing = dict()
    explored = set()
    leaders = dict()
    t = 0
    global N

    for vertex in range(N, 0, -1):
        if vertex in explored:
            continue

        s = vertex # leader node
        stack = [vertex]
        while stack:
            u = stack.pop()
            if u not in explored: # explored node has all edges in stack
                explored.add(u)
                stack.append(u) # add back u to stack before its edges
                if u in graph:   # add the edges of u to the stack
                    for v in graph[u]:
                        if v not in explored:
                            stack.append(v)
            else:
                if u not in finishing:
                    t +=1
                    finishing[u] = t
                    leaders[u] = s
    return finishing, leaders



def SCC(graph, graph_rev):
    # not all vertecs in both graphs. find the maximum number
    global N
    N = max(max(graph.keys()), max(graph_rev.keys()))

    # 1st DFS loop on reverse graph to get finishing order, ignore leaders
    finishing, _ = DFS(graph_rev)

    # replace the node with finishing order to get new graph
    time_graph = dict()
    for i in graph:
        time_nodes = set()
        for j in graph[i]:
            time_nodes.add(finishing[j])
        time_graph[finishing[i]] = time_nodes


    # 2nd DFS loop on graph to get leaders, ignore finishing time
    _, leaders = DFS(time_graph)


    # group nodes to scc
    # the results leaders and nodes are replaced by finishing time
    components = dict()
    for node, leader in leaders.iteritems():
        c = components.get(leader, set())
        c.add(node)
        components[leader] = c

    size = sorted([len(i) for i in components.values()], reverse = True)
    return size[:5] # return the first five biggest scc

####################################
graph, graph_rev = readData("SCC.txt")
#print "graph", graph
#print "reverse", graph_rev
print "done reading graph"

import time
start = time.time()
print SCC(graph, graph_rev)
print "time eclapsed", time.time()-start, "seconds"
