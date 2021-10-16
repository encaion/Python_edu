# https://networkx.org/

# !pip install --upgrade pip --user
# !pip install networkx
# !pip install matplotlib

import matplotlib.pyplot as plt
import networkx as nx

G = nx.petersen_graph()
subax1 = plt.subplot(121)
nx.draw(G, with_labels = True, font_weight = "bold")
subax2 = plt.subplot(122)
nx.draw_shell(G, nlist = [range(5, 10), range(5)], with_labels = True, font_weight = "bold")
