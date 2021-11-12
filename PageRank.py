from pygraph.classes.digraph import digraph
import pandas as pd
from time import *
import dask.dataframe as dd


class PRIterator:
    __doc__ = '''计算一张图中的PR值'''

    def __init__(self, dg):
        self.damping_factor = 0.85  # Damping factor, α
        self.max_iterations = 100  # Maximum number of iterations
        self.min_delta = 0.00001  # Parameters to determine if an iteration is finished,即ϵ
        self.graph = dg

    def page_rank(self):
        #  First change the nodes in the graph that have no outgoing chains to have outgoing chains for all nodes
        for node in self.graph.nodes():
            if len(self.graph.neighbors(node)) == 0:
                for node2 in self.graph.nodes():
                    digraph.add_edge(self.graph, (node, node2))
        nodes = self.graph.nodes()
        graph_size = len(nodes)

        if graph_size == 0:
            return {}
        page_rank = dict.fromkeys(nodes, 1.0 / graph_size)  # Assign an initial PR value to each node
        damping_value = (1.0 - self.damping_factor) / graph_size  # The (1 - α)/N part of the formula

        flag = False

        for i in range(self.max_iterations):
            change = 0
            for node in nodes:
                rank = 0
                for incident_page in self.graph.incidents(node):  # Iterate through all "incoming" pages
                    rank += self.damping_factor * (page_rank[incident_page] / len(self.graph.neighbors(incident_page)))
                rank += damping_value
                change += abs(page_rank[node] - rank)  # Absolute values
                page_rank[node] = rank

            print("This is NO.%s iteration" % (i + 1))
            # print(page_rank)
            if change < self.min_delta:
                flag = True
                break

        if flag:
             print("finished in %s iterations!" % node)
        else:
            print("finished out of 100 iterations!")
        return page_rank


if __name__ == '__main__':
    time0 = time()
    data0 = dd.read_csv("C:/Users/blair/Desktop/data/TestTime/Airport4.csv",
                        encoding='gbk')
    data1 = dd.read_csv("C:/Users/blair/Desktop/data/TestTime/Route4.csv", encoding='gbk')
    dg = digraph()
    dg.add_nodes(data0["ID"].compute())
    aaa = data1["Departure"].compute()
    bbb = data1["Destination"].compute()
    for i in range(len(aaa)):
        dg.add_edge((aaa[i], bbb[i]))
    pr = PRIterator(dg)
    page_ranks = pr.page_rank()
    dataframe = pd.DataFrame({'name': page_ranks})
    score = 0
    for i in dataframe.values:
        score += i[0]
    print(score)

    print("The final page rank is\n", page_ranks)
    time1 = time()
    print("111", time1 - time0)

