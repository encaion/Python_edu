import pandas as pd
df_pairs = pd.DataFrame(dict(u = [0, 0, 1, 2, 3, 3, 4, 5, 6, 6, 7, 8, 9, 10, 11, 12, 12],
                             v = [1, 2, 2, 3, 9, 8, 5, 6, 5, 7, 5, 6, 7,  8,  9, 10,  3]))

import plotly.graph_objects as go
import networkx as nx

def graph_genarator(data, edge_iloc_u = 0, edge_iloc_v = 1, fig_width = 400, fig_height = 300):
    G_base = nx.Graph()
    for n_node in range(len(data)):
        G_base.add_node(n_node)
        G_base.add_edge(u_of_edge = data.iloc[n_node, edge_iloc_u], v_of_edge = data.iloc[n_node, edge_iloc_v])
    
    pos = nx.kamada_kawai_layout(G_base)
    
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
    fig.update_layout(width = fig_width, height = fig_height)
    return fig
  
graph_genarator(df_pairs).show()
