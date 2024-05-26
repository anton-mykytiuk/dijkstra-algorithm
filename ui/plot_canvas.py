from matplotlib.backends.backend_qt5agg import FigureCanvas
import networkx as nx
import matplotlib.pyplot as plt


class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None):
        super().__init__(plt.figure())
        self.setParent(parent)

    def plot(self, graph, shortest_path=None):
        self.figure.clf()
        pos = nx.spring_layout(graph, seed=42)

        labels = nx.get_edge_attributes(graph, 'weight')

        nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold', edge_color='gray',
                width=1.5, arrows=True)

        if shortest_path:
            edges = [(shortest_path[n], shortest_path[n + 1]) for n in range(len(shortest_path) - 1)]
            nx.draw_networkx_edges(graph, pos, edgelist=edges, edge_color='r', width=4)

        nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels, font_color='red')

        self.draw_idle()
