import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
#sql query to get transactions
#transactions between entities (accounts, customers and bank) will be implemented into a directed graph
G.add_edges_from([(901,902), (902,901), (901,903), (903,902)])

pos = nx.spring_layout(G)
#displays graph as a plot for visual purpose (wont be used in final app, just there for understanding)
nx.draw_networkx_nodes(G, pos, node_size=500)
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='black')
nx.draw_networkx_labels(G, pos)
#simple_cycles() functions shows cycles in the graph --> the cycles are what cause the deadlock
print(list(nx.simple_cycles(G)))
plt.show()