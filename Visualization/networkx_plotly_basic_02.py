import plotly.graph_objects as go
import networkx as nx

G = nx.Graph()

for n_node in range(20):
    G.add_node(n_node)

G.add_edge(u_of_edge = 0, v_of_edge = 1)
G.add_edge(u_of_edge = 0, v_of_edge = 2)
G.add_edge(u_of_edge = 1, v_of_edge = 2)
G.add_edge(u_of_edge = 2, v_of_edge = 3)
G.add_edge(u_of_edge = 3, v_of_edge = 4)
G.add_edge(u_of_edge = 3, v_of_edge = 8)
G.add_edge(u_of_edge = 4, v_of_edge = 5)
G.add_edge(u_of_edge = 5, v_of_edge = 6)
G.add_edge(u_of_edge = 6, v_of_edge = 5)
G.add_edge(u_of_edge = 6, v_of_edge = 7)

for n_edge in range(7, 20):
    G.add_edge(u_of_edge = n_edge, v_of_edge = n_edge - 2)

pos = nx.spectral_layout(G)

fig_size = dict(width = 400,
                height = 300)

edge_x = []
edge_y = []
for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_x.extend([x0, x1, None])
    edge_y.extend([y0, y1, None])
    
edge_trace = go.Scatter(x = edge_x, y = edge_y,
                        line = dict(width = 0.5, color = '#888'),
                        hoverinfo = "none",
                        mode = "lines")

node_x = []
node_y = []
node_deg = []
node_col = []
for node in G.nodes():
    node_x.append(pos[node][0])
    node_y.append(pos[node][1])
    node_deg.append(G.degree[node] * 5)
    node_col.append(G.degree[node])
    
node_trace = go.Scatter(x = node_x, y = node_y,
                        mode = "markers",
                        hoverinfo = "text",
                        marker = dict(showscale = True,
                                      colorscale = "Rainbow",
                                      reversescale = True,
                                      color = node_col,
                                      size = node_deg,
                                      colorbar = dict(thickness = 15,
                                                      title = "Node Connections",
                                                      xanchor = "left",
                                                      titleside = "right"),
                                      line_width = 2))

node_text = []
for node, adjacencies in enumerate(G.adjacency()):
    node_text.append("#{node_number}, Deg.: {deg}".format(node_number = node,
                                                          deg = str(len(adjacencies[1]))))

node_trace.text = node_text

fig = go.Figure(data = [edge_trace, node_trace],
                layout = go.Layout(showlegend = False,
                                   hovermode = "closest",
                                   plot_bgcolor = "white",
                                   margin = dict(b = 0, l = 0, r = 0, t = 40),
                                   xaxis = dict(showgrid = False, zeroline = False, showticklabels = False),
                                   yaxis = dict(showgrid = False, zeroline = False, showticklabels = False)))
fig.update_layout(width = fig_size["width"], height = fig_size["height"])
fig.show()
