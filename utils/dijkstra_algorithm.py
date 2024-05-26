class DijkstraAlgorithm:
    def __init__(self, graph):
        self.graph = graph

    def find_route(self, start, end):
        visited = {}
        parents = {}
        unvisited = {}
        for node in self.graph:
            unvisited[node] = 0 if node == start else float("inf")

        while unvisited:
            current_node = min(unvisited, key=unvisited.get)

            for neighbour, weight in self.graph[current_node].items():
                if neighbour in visited:
                    continue

                if unvisited[current_node] + weight["weight"] < unvisited[neighbour]:
                    unvisited[neighbour] = unvisited[current_node] + weight["weight"]
                    parents[neighbour] = current_node

            visited[current_node] = unvisited[current_node]
            unvisited.pop(current_node)

            if current_node == end:
                break
        return parents, visited

    @staticmethod
    def generate_path(parents, start, end):
        path = [end]
        while True:
            key = parents[path[0]]
            path.insert(0, key)
            if key == start:
                break
        return path
