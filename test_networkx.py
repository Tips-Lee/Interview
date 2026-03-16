import networkx as nx
import matplotlib.pyplot as plt

"""
# 创建一个加权图
G = nx.Graph()
G.add_weighted_edges_from([
 ('A', 'B', 2),
 ('A', 'C', 4),
 ('B', 'C', 1),
 ('B', 'D', 7),
 ('C', 'D', 3),
 ('C', 'E', 5),
 ('D', 'E', 2),
 ('D', 'F', 1),
 ('E', 'F', 3)
])

# 计算无权最短路径
unweighted_path = nx.shortest_path(G, source='A', target='F')

unweighted_length = nx.shortest_path_length(G, source='A', target='F')
# 计算加权最短路径（Dijkstra算法）
weighted_path = nx.shortest_path(G, source='A', target='F', weight='weight')
weighted_length = nx.shortest_path_length(G, source='A', target='F',
weight='weight')
print(f'无权最短路径: {unweighted_path}, 长度: {unweighted_length}')
print(f'加权最短路径: {weighted_path}, 长度: {weighted_length}')
# 可视化图和最短路径
pos = nx.spring_layout(G)
plt.figure(figsize=(12, 8))
# 绘制整个图
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500,
font_size=12)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
# 高亮显示加权最短路径
path_edges = list(zip(weighted_path, weighted_path[1:]))
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2.5)
plt.title('Weighted Shortest Path Analysis')
plt.axis('off')
plt.show()
"""
# 创建一个社交网络示例
G = nx.karate_club_graph()
# 计算各种中心性指标
degree_centrality = nx.degree_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)
closeness_centrality = nx.closeness_centrality(G)
eigenvector_centrality = nx.eigenvector_centrality(G)
# 打印每个节点的中心性（只显示前5个节点）
print('节点\t度中心性\t介数中心性\t接近中心性\t特征向量中心性')
for node in list(G.nodes)[:5]:
    print(node)

print(G.nodes.values())
    # print(f'{node}\t{degree_centrality[node]:.4f}\t\t{betweenness_centrality[node]:.4f}\t\t{closeness_centrality[node]:.4f}\t\t{eigenvector_centrality[node]:.4f}')
# 可视化节点的度中心性
plt.figure(figsize=(12, 10))
# 根据度中心性设置节点大小
node_size = [v * 10000 for v in degree_centrality.values()]
# 根据节点的社团划分设置节点颜色
colors = []
for node in G.nodes():
    if G.nodes[node]['club'] == 'Mr. Hi':
        colors.append('blue')
    else:
        colors.append('red')
# 绘制网络
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, node_color=colors, node_size=node_size, with_labels=True,font_size=10, font_color='white', edge_color='gray')
plt.title('Zacharys karate club network degree centrality analysis')
plt.axis('off')
plt.show()

