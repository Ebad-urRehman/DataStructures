#adjacency List representation for graphs data structure
class AdjacencyNode:
    def __init__(self, data):
        self.node_data = data
        self.status = 1
        # status 1 = ready state
        # status 2 = waiting state
        # status 3 = proccessed state

class AdjacencyList:
    def __init__(self, edges):

        self.root = edges[0][0]
        self.status_dict = {}
        self.graph_dict = {}
        for start, end in edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
            # setting status for all nodes
            if start not in self.status_dict:
                self.status_dict[start] = 1
            if end not in self.status_dict:
                self.status_dict[end] = 1
        print("root", self.root)
        print("Graph Dict:", self.graph_dict)
        print("Status Dict:", self.status_dict)

        
    def BFS(self):
        root = self.root
        self.status_dict[root] = 2
        my_queue = []
        while root is not None:
            if root in self.graph_dict:
                for neighbor_node in self.graph_dict[root]:
                    if self.status_dict[neighbor_node] == 1:
                        my_queue.insert(0, neighbor_node)
                        self.status_dict[neighbor_node] = 2
                self.status_dict[root] = 3
                # print(root)
                # print(self.status_dict)
                
                
            # meaning poped element is not in source nodes its a sink node
            else:
                self.status_dict[root] = 3
                print(self.status_dict)
            if len(my_queue) >= 1:
                root = my_queue.pop(-1)
            else:
                root = None
                
        #

if __name__ == "__main__":
    vertices = ["A", "B", "C", "D"]
    edges = [
        ("A","B"),
        ("A", "C"),
        ("A", "D"),
        ("C","B"),
        ("C","D"),
        ("B","D"),
    ]

    my_adj_list = AdjacencyList(edges)
    my_adj_list.BFS()
    