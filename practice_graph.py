"""
Practice graphs
"""
from collections import defaultdict, deque

class Graph(object):
    """
    Class for a graph
    """
    def __init__(self):
        """
        Constructor
        """
        self.edges = defaultdict(defaultdict)
        self.search = {'bfs':deque.popleft, 'dfs': deque.pop}

    def add_edge(self, edge_u, edge_v, cost):
        """
        Adding edges to the graph
        """
        self.edges[edge_u][edge_v] = cost
        self.edges[edge_v][edge_u] = cost

    def dfs(self, source):
        """
        Performing dfs from the source
        """
        bfs_stack = deque()
        bfs_stack.append(source)
        visited = defaultdict()
        path = ""

        while bfs_stack:
            current_node = bfs_stack.pop()

            if visited.get(current_node, 0):
                continue
            path += str(current_node) + " "
            visited[current_node] = 1
            neighbours = self.edges[current_node].keys()
            bfs_stack.extend(neighbours)

        print path

    def bfs(self, source):
        """
        Performing bfs from the source
        """
        dfs_queue = deque()
        visited = defaultdict()
        path = ""
        dfs_queue.append(source)

        while dfs_queue:
            current_node = dfs_queue.popleft()

            if visited.get(current_node, 0):
                continue

            path += current_node + " "

            visited[current_node] = 1

            neighbors = self.edges[current_node].keys()
            dfs_queue.extend(neighbors)

        print path

    def generic_search(self, source, destination, search_method):
        """
        Function which perform bfs/dfs based on the specified_method
        """

        double_queue = deque()
        double_queue.append(source)
        visited = defaultdict()
        path = ""

        print "___________________________"
        print "Performing " + search_method
        print ""
        method = self.search[search_method]

        while double_queue:
            current_node = method(double_queue)

            if visited.get(current_node, 0):
                continue

            path += str(current_node) + " "

            if current_node == destination:
                break

            visited[current_node] = 1
            neighbours = self.edges[current_node].keys()
            double_queue.extend(neighbours)

        print path

    def minimum_distance(self, source, destination):
        """
        """
        

def main():
    """
    main function
    """
    my_graph = Graph()

    my_graph.add_edge("1", "2", 1)
    my_graph.add_edge("1", "3", 1)
    my_graph.add_edge("1", "4", 1)
    my_graph.add_edge("2", "4", 1)
    my_graph.add_edge("2", "5", 1)
    my_graph.add_edge("5", "6", 1)
    my_graph.add_edge("3", "6", 1)

    my_graph.bfs("6")
    my_graph.dfs("3")

    my_graph.generic_search("1", "6", "bfs")
    my_graph.generic_search("1", "6", "dfs")

if __name__ == "__main__":
    #execute only if this module is called directly
    main()
