import networkx as nx

def read_graph(file_name):
    with open(file_name) as f:
        edges_lines = f.readlines()
    edges_lines = [x.strip() for x in edges_lines]
    g = nx.Graph()
    edges = [(int(e.split()[0]), int(e.split()[1])) for e in edges_lines]
    g.add_edges_from(edges)
    return g

# read the graph file
g = read_graph("input/some_file.graph")


def btw(g, w):

    # if numbe of node in path = 4 then len of path will be 3
    # to calculate 3 btw-centrality
    l = 4

    def sigma(u, v, l):
        paths = list(nx.all_shortest_paths(g, source=u, target=v))
        return len([path for path in paths if len(path) == l])

    def sigma_w(u, v, w, l):
        paths = list(nx.all_shortest_paths(g, source=u, target=v))
        return len([path for path in paths if len(path) == l and w in path])

    # create the two sets and exclude w node
    U = [n for n in g.nodes if (n % 2 == 0 and n != w)]
    V = [n for n in g.nodes if (n % 2 == 1 and n != w)]

    # Σ𝜎𝑢𝑣(𝑙,𝑤)𝜎𝑢𝑣(𝑙) where u!=v!=w and 𝑢∈U and v∈V

    summation = 0
    for u in U:
        for v in V:
            if(sigma(u, v, l) != 0):
                num = sigma_w(u, v, w, l)
                den = sigma(u, v, l)
                fraction = num / den
                summation = summation + fraction

    print("Completed for " + str(w))
    return round(summation, 3)


btw_g = [btw(g, w) for w in sorted(g.nodes)]

file = open("ans.output", "w")
file.write("\t".join([str(node) for node in btw_g]))
file.close()
