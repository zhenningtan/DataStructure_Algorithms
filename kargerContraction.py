# read in the list
def ReadGraph(file):
    array = []
    with open(file, "r") as f:
        for line in f:
            row = line.strip().split()
            irow = [int(x) for x in row]
            if irow:
                array.append(irow)
    return array


import random
import copy

def RContraction(graph):
    ''' input graph is a list of lists. The first column
    in the file represents the vertex label, and the particular row
    (other entries except the first column) tells all the vertices
    that the vertex is adjacent to.
    '''
    if len(graph) < 2:
        return "Error: there are less than 2 vetices"
    else:
        while len(graph) >2:
            #print "number of vertics:", len(graph)
            #1. random select an edge with two vertices
            #extract the vertics to a list and ran
            v = [vx[0] for vx in graph]
            v1 = random.choice(v)
            v1ind = v.index(v1)
            v2 = random.choice(graph[v1ind][1:])
            v2ind = v.index(v2)
            #2. add v2 edges to v1
            graph[v1ind] = graph[v1ind] + graph[v2ind][1:]
            #print "before  removing self loop:", graph[v1ind]
            #3. replace v2 with v1 for all v2
            for vertix in graph:
                for i in range(1, len(vertix)):
                    if vertix[i] == v2:
                        vertix[i] = v1
            #4. remove self loops
            v1e = graph[v1ind][1:]
            graph[v1ind] = [graph[v1ind][0]]
            for e in v1e:
                if e != v1:
                    graph[v1ind].append(e)
            #print "after removing self loop:", graph[v1ind]
            #5. delete the contracted second vertix
            del graph[v2ind]

        # verify leftover edges
        if len(graph[0]) == len(graph[1]):
            mincut = len(graph[0]) -1
            return mincut
        else:
            return "uneual edges"

# read in data file
array = ReadGraph("kargerMinCut.txt")
n = len(array)
print "length of graph:", n

N = 1000
print "number of runs:", N

mincutl = []
error = 0
import time
start = time.time()

# run the contraction N times to store the minimum cut into a list
# and find the smallest number
for i in range(N):
    graph = copy.deepcopy(array)
    mincut = RContraction(graph)
    if isinstance(mincut, int):
        mincutl.append(mincut)
    else:
        error +=1

samllest = min(mincutl)
print "the minimum cut is", samllest
print "run time:", time.time()-start
print "error:", error
