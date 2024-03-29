"""
This is the graph module. It contains a minimalistic Graph class.
"""


class Graph:
    """
    A class representing undirected graphs as adjacency lists.

    Attributes
    ----------
    nodes: NodeType
        A list of nodes. Nodes can be of any immutable type, e.g., integer,
        float, or string.
        We will usually use a list of integers 1, ..., n.
    graph: dict
        A dictionary that contains the adjacency list of each node in the form
        graph[node] = [neighbor1, neighbor2, ...]
    nb_nodes: int
        The number of nodes.
    nb_edges: int
        The number of edges.
    edges: list[tuple[NodeType, NodeType]]
        The list of all edges
    """

    def __init__(self, nodes: list = None):
        """
        Initializes the graph with a set of nodes, and no edges.

        Parameters
        ----------
        nodes: list, optional
            A list of nodes. Default is empty.
        """
        if nodes is None:
            self.nodes = []
        else:
            self.nodes = nodes
        self.graph = dict([(n, []) for n in nodes])
        self.nb_nodes = len(nodes)
        self.nb_edges = 0
        self.edges = []

    def __str__(self) -> str:
        """
        Returns a string that lists the neighbors for each node in the graph,
        one node per line

        Returns
        -------
        output: str
            A string representation of the graph, including a header
            line and one list of the connections of every nodes.
        """
        if not self.graph:
            output = "The graph is empty"
        else:
            output = (f"The graph has {self.nb_nodes} nodes "
                      f"and {self.nb_edges} edges.\n")
            for source, destination in self.graph.items():
                output += f"{source}-->{destination}\n"
        return output

    def __repr__(self) -> str:
        """
        Returns a representation of the graph with number of nodes and edges.

        Returns
        -------
        output: str
            A formal representation of the graph, indicating its class,
            number of nodes (nb_nodes), and number of edges (nb_edges).
        """
        output = (f"<graph.Graph: nb_nodes={self.nb_nodes}, "
                  f"nb_edges={self.nb_edges}>")
        return output

    def add_edge(self, node1, node2):
        """
        Adds an edge to the graph. Graphs are not oriented, hence an edge is
        added to the adjacency list of both end nodes.
        When adding an edge between two nodes, if one of the nodes does not
        exist it is added to the list of nodes.

        Parameters
        ----------
        node1: NodeType
            First end (node) of the edge
        node2: NodeType
            Second end (node) of the edge

        Raises
        ------
        Exception
            The edge you are trying to add already exist
        """
        if (node1, node2) in self.edges or (node2, node1) in self.edges:
            raise Exception("edge already exist")
        else:
            if node1 not in self.graph:
                self.graph[node1] = [node2]
                self.nb_nodes += 1
                self.nodes.append(node1)
            else:
                self.graph[node1].append(node2)
            if node2 not in self.graph:
                self.graph[node2] = [node1]
                self.nb_nodes += 1
                self.nodes.append(node2)
            else:
                self.graph[node2].append(node1)

            self.nb_edges += 1
            self.edges.append((node1, node2))

    def bfs(self, src, dst):
        """
        Finds a shortest path from src to dst by BFS.

        Parameters
        ----------
        src: NodeType
            The source node.
        dst: NodeType
            The destination node.

        Returns
        -------
        path: list[NodeType] | None
            The shortest path from src to dst. Returns None if dst is not
            reachable from src
        """
        # TODO: Implement this function
        # NOTE: Remove the line "raise NotImplementedError"
        raise NotImplementedError

    @classmethod
    def graph_from_file(cls, file_name: str):
        """
        Reads a text file and returns the graph as an object of the Graph
        class.

        The file should have the following format:
            The first line of the file is 'n m'
            The next m lines have 'node1 node2'
        The nodes (node1, node2) should be named 1..n

        Parameters
        ----------
        file_name: str
            The name of the file

        Returns
        -------
        graph: Graph
            An object of the class Graph with the graph from file_name.
        """
        with open(file_name, "r") as file:
            n, m = map(int, file.readline().split())
            graph = Graph(range(1, n+1))
            for _ in range(m):
                edge = list(map(int, file.readline().split()))
                if len(edge) == 2:
                    node1, node2 = edge
                    graph.add_edge(node1, node2)  # Will add dist=1 by default
                else:
                    raise Exception("Format incorrect")
        return graph
