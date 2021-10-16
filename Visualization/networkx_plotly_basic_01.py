import plotly.graph_objects as go
import networkx as nx

G = nx.Graph()

G.add_node(0, pos = (0.5, 1.5))
G.add_node(1, pos = (1.5, 1.5))

G.add_edge(u_of_edge = 0, v_of_edge = 1)


edge_x = []
edge_y = []
for edge in G.edges():
    x0, y0 = G.nodes[edge[0]]['pos']
    x1, y1 = G.nodes[edge[1]]['pos']
    edge_x.extend([x0, x1, None])
    edge_y.extend([y0, y1, None])
    
edge_trace = go.Scatter(x = edge_x, y = edge_y,
                        line = dict(width = 0.5, color = '#888'),
                        hoverinfo = "none",
                        mode = "lines")

node_x = []
node_y = []
for node in G.nodes():
    x, y = G.nodes[node]['pos']
    node_x.append(x)
    node_y.append(y)
    
node_trace = go.Scatter(x = node_x, y = node_y,
                        mode = "markers",
                        hoverinfo = "text",
                        marker = dict(showscale = True,
                                      colorscale = "YlGnBu",
                                      reversescale = True,
                                      color = [],
                                      size = [10, 20, 30],
                                      colorbar = dict(thickness = 15,
                                                      title = "Node Connections",
                                                      xanchor = "left",
                                                      titleside = "right"),
                                      line_width = 2))

node_adjacencies = []
node_text = []
for node, adjacencies in enumerate(G.adjacency()):
    node_adjacencies.append(len(adjacencies[1]))
    node_text.append('Degree: ' + str(len(adjacencies[1])))

node_trace.marker.color = node_adjacencies
node_trace.text = node_text


fig = go.Figure(data = [edge_trace, node_trace],
                layout = go.Layout(showlegend = False,
                                   hovermode = "closest",
                                   margin = dict(b = 0, l = 0, r = 0, t = 40),
                                   xaxis = dict(showgrid = False, zeroline = False, showticklabels = False),
                                   yaxis = dict(showgrid = False, zeroline = False, showticklabels = False)))
fig.show()
