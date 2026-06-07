import heapq

class Router:

    @staticmethod
    def calculate_travel_time(
        distance,
        speed
    ):
        return (distance / speed) * 60

    @classmethod
    def shortest_path(
        cls,
        graph,
        start,
        target,
        optimize_by="distance"
    ):

        costs = {
            node: float("inf")
            for node in graph.nodes
        }

        previous = {
            node: None
            for node in graph.nodes
        }

        costs[start] = 0

        pq = []
        heapq.heappush(pq, (0, start))

        while pq:

            current_cost, current_node = heapq.heappop(pq)

            if current_node == target:
                break

            for neighbor, dist, speed in graph.get_neighbors(current_node):

                if optimize_by == "time":
                    edge_cost = cls.calculate_travel_time(
                        dist,
                        speed
                    )
                else:
                    edge_cost = dist

                new_cost = current_cost + edge_cost

                if new_cost < costs[neighbor]:

                    costs[neighbor] = new_cost
                    previous[neighbor] = current_node

                    heapq.heappush(
                        pq,
                        (new_cost, neighbor)
                    )

        path = []
        current = target

        while current is not None:
            path.append(current)
            current = previous[current]

        path.reverse()

        if path and path[0] == start:
            return path, costs[target]

        return None, float("inf")

    @classmethod
    def route_summary(
        cls,
        graph,
        path,
        optimize_by
    ):

        total_distance = 0
        total_time = 0

        for i in range(len(path) - 1):

            u = path[i]
            v = path[i + 1]

            for neighbor, dist, speed in graph.get_neighbors(u):

                if neighbor == v:

                    total_distance += dist

                    total_time += (
                        cls.calculate_travel_time(
                            dist,
                            speed
                        )
                    )

                    break

        return {
            "path": path,
            "distance": round(total_distance, 2),
            "time": round(total_time, 2),
            "optimized_by": optimize_by
        }
        # ....