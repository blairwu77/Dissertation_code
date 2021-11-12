import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt


a = nx.read_edgelist("C:/Users/blair/Desktop/data/TestTime/networkxtest.csv", delimiter=",", create_using=nx.DiGraph())

pr_dict = nx.pagerank(a)
print(pr_dict)

