def readData(filename):
	graph = {}
	with open(filename,'r') as f:
		for line in f:
			line = line.rstrip().split()
			if line:
				v = int(line[0])
				graph[v] = {}
				for e in line[1:]:
					e, weight = e.split(",")
					e, weight = int(e), int(weight)
					graph[v][e] = weight

	return graph

g = readData("dijkstraData.txt")
#print g


def dijkstra_shortest_path(graph, node):
	#calcuate the shortest path from the node to any other node in the graph
	X = set([node])	# processed nodes so far
	A = {node: 0}		# computed shortest path distances
	B = {node: [node]}		# contains shorted path for each node

	V = set(graph.keys())	# get all vertices
	while X!= V:
		shortest = 100000
		for v in X:
			for w, weight in graph[v].items():
				if w not in X:
					dist = A[v] + weight
					if dist <= shortest:
						shortest = dist
						ws = w
						vs = v
		X.add(ws)
		A[ws] = shortest
		B[ws] = B[vs]
		B[ws].append(ws)
	return A

A = dijkstra_shortest_path(g,1)
print "A", A
