# plotly 결과물 왼쪽 하단에 "new_text" 텍스트가 표기되는데 이는 annotation과 관련이 있다.
# 이는 annotation 인자의 텍스트에 값이 할당되어있지 않기 때문.

# 하단 new_text 가 나오는 경우 1
fig = go.Figure(data = [edge_trace, node_trace],
                layout = go.Layout(annotations = [dict(showarrow = False,
                                                       xref = "paper", yref = "paper",
                                                       x = 0.005, y = -0.002)],
                                   xaxis = dict(showgrid = False, zeroline = False, showticklabels = False),
                                   yaxis = dict(showgrid = False, zeroline = False, showticklabels = False)))
fig.show()

# 하단 new_text 가 나오는 경우 2
fig = go.Figure(data = [edge_trace, node_trace],
                layout = go.Layout(annotations = [dict(text = None,
                                                       showarrow = False,
                                                       xref = "paper", yref = "paper",
                                                       x = 0.005, y = -0.002)],
                                   xaxis = dict(showgrid = False, zeroline = False, showticklabels = False),
                                   yaxis = dict(showgrid = False, zeroline = False, showticklabels = False)))
fig.show()

# 하단 new_text 가 나오는 않는 경우 1
fig = go.Figure(data = [edge_trace, node_trace],
                layout = go.Layout(annotations = [dict(text = "aaaa", 
                                                       showarrow = False,
                                                       xref = "paper", yref = "paper",
                                                       x = 0.005, y = -0.002)],
                                   xaxis = dict(showgrid = False, zeroline = False, showticklabels = False),
                                   yaxis = dict(showgrid = False, zeroline = False, showticklabels = False)))
fig.show()

# 하단 new_text 가 나오는 않는 경우 2
fig = go.Figure(data = [edge_trace, node_trace],
                layout = go.Layout(xaxis = dict(showgrid = False, zeroline = False, showticklabels = False),
                                   yaxis = dict(showgrid = False, zeroline = False, showticklabels = False)))
fig.show()
