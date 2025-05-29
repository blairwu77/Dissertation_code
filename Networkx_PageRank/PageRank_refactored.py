from pygraph.classes.digraph import digraph
import pandas as pd
from time import time
import dask.dataframe as dd


class PRIterator:
    """
    PageRank computation for a directed graph.
    """

    def __init__(self, dg):
        self.damping_factor = 0.85  # Damping factor α
        self.max_iterations = 100  # Max number of iterations
        self.min_delta = 0.00001   # Convergence threshold ε
        self.graph = dg

    def page_rank(self):
        # Add outgoing edges from dangling nodes (nodes with no outlinks) to all nodes
        for node in self.graph.nodes():
            if len(self.graph.neighbors(node)) == 0:
                for node2 in self.graph.nodes():
                    digraph.add_edge(self.graph, (node, node2))

        nodes = self.graph.nodes()
        graph_size = len(nodes)

        if graph_size == 0:
            return {}

        # Initialize all PR values equally
        page_rank = dict.fromkeys(nodes, 1.0 / graph_size)
        damping_value = (1.0 - self.damping_factor) / graph_size

        for i in range(self.max_iterations):
            change = 0
            for node in nodes:
                rank = 0
                for incident_page in self.graph.incidents(node):  # Iterate all incoming links
                    rank += self.damping_factor * (
                        page_rank[incident_page] / len(self.graph.neighbors(incident_page))
                    )
                rank += damping_value
                change += abs(page_rank[node] - rank)
                page_rank[node] = rank

            print(f"Iteration #{i + 1}")
            if change < self.min_delta:
                print(f"Converged in {i + 1} iterations.")
                break
        else:
            print("Reached maximum iteration limit without convergence.")

        return page_rank


if __name__ == '__main__':
    start_time = time()

    # Load airport and route data
    airports_df = dd.read_csv("C:/Users/blair/Desktop/data/TestTime/Airport4.csv", encoding='gbk')
    routes_df = dd.read_csv("C:/Users/blair/Desktop/data/TestTime/Route4.csv", encoding='gbk')

    dg = digraph()
    dg.add_nodes(airports_df["ID"].compute())

    departures = routes_df["Departure"].compute()
    destinations = routes_df["Destination"].compute()

    for i in range(len(departures)):
        dg.add_edge((departures[i], destinations[i]))

    pr = PRIterator(dg)
    page_ranks = pr.page_rank()

    # Sum all PR values for validation
    total_score = sum(page_ranks.values())
    print(f"Total PR score: {total_score:.4f}")

    print("Final PageRank results:\n", page_ranks)

    end_time = time()
    print("Execution time (s):", end_time - start_time)
