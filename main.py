import sys

graph = {'A': {'B': 2, 'D': 8},
         'B': {'A': 2, 'E': 6, 'D': 5},
         'D': {'B': 5, 'A': 8, 'E': 3, 'F': 2},
         'E': {'B': 6, 'F': 1, 'C': 9, 'D': 3},
         'F': {'C': 3, 'E': 1, 'D': 2},
         'C': {'E': 9, 'F': 3}}

src = 'A'
dest = 'C'
visited = []
unvisited = []
nodeData = {}
unvisited.append(src)

for i in graph:
    nodeData[i] = {'shortestDistance': sys.maxsize, 'prevNode': None}
    if i not in unvisited:
        unvisited.append(i)

nodeData[src]['shortestDistance'] = 0


def leastDistance():
    l = {}
    for i in nodeData:
        if i not in visited:
            l[i] = nodeData[i]['shortestDistance']
    return min(l, key=l.get)


while unvisited != []:
    currentPos = leastDistance()
    if currentPos not in visited:
        for j in graph[currentPos]:
            d = graph[currentPos][j] + nodeData[currentPos]['shortestDistance']
            if d < nodeData[j]['shortestDistance']:
                nodeData[j]['shortestDistance'] = d
                nodeData[j]['prevNode'] = currentPos
        unvisited.remove(currentPos)
        visited.append(currentPos)

print(nodeData)

shortestPath = [dest]
while shortestPath[-1] != src:
    x = shortestPath[-1]
    shortestPath.append(nodeData[x]['prevNode'])
shortestPath.reverse()
print(shortestPath)