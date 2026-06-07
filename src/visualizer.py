import networkx as nx
import matplotlib.pyplot as plt


class Visualizer:

    @staticmethod
    def draw(
        graph,
        path=None,
        return_figure=False
    ):

        G = nx.Graph()

        pos = {}

        for node, coords in graph.nodes.items():

            G.add_node(node)

            pos[node] = (
                coords["lon"],
                coords["lat"]
            )

        for u in graph.adjacency_list:

            for v, dist, _ in graph.get_neighbors(u):

                if not G.has_edge(u, v):

                    G.add_edge(
                        u,
                        v,
                        weight=dist
                    )

        fig, ax = plt.subplots(
            figsize=(10, 7)
        )

        nx.draw(
            G,
            pos,
            with_labels=True,
            node_size=2000,
            ax=ax
        )

        labels = nx.get_edge_attributes(
            G,
            "weight"
        )

        nx.draw_networkx_edge_labels(
            G,
            pos,
            edge_labels=labels,
            ax=ax
        )

        if path:

            edges = list(
                zip(
                    path[:-1],
                    path[1:]
                )
            )

            nx.draw_networkx_edges(
                G,
                pos,
                edgelist=edges,
                width=4,
                ax=ax
            )

        if return_figure:
            return fig

        plt.show()
        # ....