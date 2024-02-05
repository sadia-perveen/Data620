#!/usr/bin/env python
# coding: utf-8

# In[1]:


import networkx as nx
import matplotlib.pyplot as plt

nx_graph = nx.Graph()

nodes = ["Andre", "Carol", "Fernando", "Diane", "Beverly", "Garth", "Ed", "Heather", "Ike", "Jane"]
nx_graph.add_nodes_from(nodes)

edges = [
    ("Carol", "Fernando"), ("Carol", "Andre"), ("Carol", "Diane"),
    ("Andre", "Carol"), ("Andre", "Diane"), ("Andre", "Beverly"), ("Andre", "Fernando"),
    ("Beverly", "Andre"), ("Beverly", "Ed"), ("Beverly", "Diane"),("Beverly", "Garth"),
    ("Ed", "Beverly"), ("Ed", "Diane"), ("Ed", "Garth"),
    ("Garth", "Ed"), ("Garth", "Diane"), ("Garth", "Fernando"),
    ("Diane", "Carol"), ("Diane", "Andre"), ("Diane", "Beverly"), ("Diane", "Ed"), ("Diane", "Garth"), ("Diane", "Fernando"),
    ("Garth", "Heather"), ("Fernando", "Heather"),
    ("Heather", "Ike"), ("Ike", "Heather"), ("Ike", "Jane"), ("Jane", "Ike")
]
nx_graph.add_edges_from(edges)

plt.figure(figsize=(10, 8))
nx.draw(nx_graph, with_labels=True, node_size=2000, node_color="lightgray", font_size=8, font_weight="bold", edge_color="purple")
plt.title('Assignment: "hello, graph world"')
plt.show()


# In[ ]:




