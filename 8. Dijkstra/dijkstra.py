network = {
    "A" : {"B" : 16, "C" : 9, "D" : 35},

    "B" : {"A" : 16, "D" : 12, "E" : 25},

    "C" : {"A" : 9, "D": 15, "F" : 22},

    "D" : {"A" : 35, "B" : 12, "C" : 15, "E" : 14, "F" : 17, "G" : 19},

    "E" : {"B" : 25, "D" : 14, "E" : 8},

    "F" : {"C" : 22, "D" : 17, "G" : 14},

    "G" : {"D" : 19, "E" : 8, "F" : 14}
}

routingMap = {}
visited = []

NODES = list(network.keys())
NETWORK_MAIN_NODE = NODES[0]

for n in network:
    routingMap[n] = {
                    "hops" :  0 if n==NETWORK_MAIN_NODE else float("inf"),

                    "pred" : "/" if n==NETWORK_MAIN_NODE else "",

                    "next-hop" : "/" if n==NETWORK_MAIN_NODE else "", 

                    "route" : "/" if n==NETWORK_MAIN_NODE else "", 
    }


def getLowerNode():
    temp = {}
    for rm in routingMap:
        if rm not in visited:
            temp[rm] = routingMap[rm]["hops"]

    return min(temp, key = temp.get)

while len(visited) < len(NODES):
    #get the CURRENT NODE
    currentNode = getLowerNode()

    #get CURRENT NODE Routes
    for node in network[currentNode]:
        if node not in visited:
            h = routingMap[currentNode]["hops"] + network[currentNode][node] 

            if(h < routingMap[node]["hops"]):
                routingMap[node]["hops"] = h
                routingMap[node]["pred"] = currentNode

    #adding to visited routers
    visited.append(currentNode)


#to get the route (e.g. => ["A", "B", "D", "E"] => A -> B -> D -> E) + get next hop (e.g. "B")
def getRoute(node):
    nodes = []
    pred = routingMap[node]["pred"]
    nodes.append(node)
    nodes.append(pred)

    while pred != NETWORK_MAIN_NODE:
        pred = routingMap[pred]["pred"]
        nodes.append(pred)
    
    return nodes[::-1]
    
for rm in routingMap:
    if rm != NETWORK_MAIN_NODE:
        route = getRoute(rm)

        routingMap[rm]["next-hop"] = route[route.index(NETWORK_MAIN_NODE)+1]
        routingMap[rm]["route"] = " -> ".join(route)
    

#NORMAL PRINT
#print(routingMap)



#



#PRETTY PRINT
for rm in routingMap:
    print(f"\n{rm} {'(MAIN NODE)' if rm == NETWORK_MAIN_NODE else ''}: \n\tHOPS => {routingMap[rm]['hops']}\n\tPREVIOUS ROUTER => {routingMap[rm]['pred']}\n\tNEXT HOP => {routingMap[rm]['next-hop']}\n\tROUTE => {routingMap[rm]['route']}\n")