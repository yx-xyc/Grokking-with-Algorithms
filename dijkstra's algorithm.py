infinity = float("inf")
""" start = {"a": 5,"b":2}
a = {"c":4,"d":2}
b = {"a":8,"d":7}
c = {"d":6,"end":3}
d = {"end": 1}
end = {}
graph = {"start":start,"a":a,"b":b,"c":c,"d":d,"end":end}
costs = {"a":5,"b":2,"c":infinity,"d":infinity,"end":infinity}
parents = {"a":"start", "b":"start"} """
start = {"a":10}
a = {"b":20}
b = {"c":1,"end":30}
c = {"a":1}
end = {}
graph = {"start":start,"a":a,"b":b,"c":c,"end":end}
costs = {"a":5,"b":2,"c":infinity,"end":infinity}
parents = {"a": "start"}
def find_lowest_cost_node(costs, processed):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node
def process_graph(graph,costs,parents):
    processed = []
    node = find_lowest_cost_node(costs,processed)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        # print(costs)
        # print(parents)
        node = find_lowest_cost_node(costs,processed)
    print(node)
    print(costs)
    print(parents)
def main(): 
    start = {"a":10}
    a = {"b":20}
    b = {"c":1,"end":30}
    c = {"a":1}
    end = {}
    graph = {"start":start,"a":a,"b":b,"c":c,"end":end}
    costs = {"a":10,"b":infinity,"c":infinity,"end":infinity}
    parents = {"a": "start"}
    process_graph(graph,costs,parents)
if __name__ == '__main__':
    main()