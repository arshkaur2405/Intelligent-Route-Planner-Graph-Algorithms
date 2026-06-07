from collections import deque

class Graph:

    def __init__(self):
        self.nodes = {}
        self.adjacency_list = {}

    def add_node(self, name, lat, lon):
        self.nodes[name] = {
            "lat": lat,
            "lon": lon
        }

        if name not in self.adjacency_list:
            self.adjacency_list[name] = []

    def add_edge(
        self,
        u,
        v,
        distance_km,
        speed_limit_kph,
        bidirectional=True
    ):

        self.adjacency_list[u].append(
            (v, distance_km, speed_limit_kph)
        )

        if bidirectional:
            self.adjacency_list[v].append(
                (u, distance_km, speed_limit_kph)
            )

    def get_neighbors(self, node):
        return self.adjacency_list.get(node, [])

    def bfs(self, start, target):

        visited = set()
        queue = deque([(start, [start])])

        while queue:

            current, path = queue.popleft()

            if current == target:
                return path

            if current not in visited:

                visited.add(current)

                for neighbor, _, _ in self.get_neighbors(current):
                    queue.append(
                        (neighbor, path + [neighbor])
                    )

        return None

    def dfs(self, start, target):

        visited = set()
        path = []

        def helper(node):

            visited.add(node)
            path.append(node)

            if node == target:
                return True

            for neighbor, _, _ in self.get_neighbors(node):

                if neighbor not in visited:

                    if helper(neighbor):
                        return True

            path.pop()
            return False

        if helper(start):
            return path

        return None
    # ...
    