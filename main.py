from PyQt5 import QtWidgets
import sys
import networkx as nx

from ui.ui import UI
from utils.dijkstra_algorithm import DijkstraAlgorithm

EMPTY_ARGUMENT = "Empty argument."


class GUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(GUI, self).__init__()
        self.form = None
        self.graph = nx.DiGraph()
        self.setup()

    def setup(self):
        self.form = UI()
        self.form.setup(self)
        self.setup_connections()
        self.form.plot_canvas.plot(self.graph)

    def setup_connections(self):
        self.form.add_node_button.clicked.connect(self.add_new_node)
        self.form.connect_button.clicked.connect(self.connect_nodes)
        self.form.run_button.clicked.connect(self.run)
        self.form.reset_graph_button.clicked.connect(self.reset)

    @staticmethod
    def show_dialog(message):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText(message)
        msg.setWindowTitle("Error")
        msg.exec_()

    def add_new_node(self):
        new_node = str(self.form.new_node_text.toPlainText())
        if not new_node:
            self.form.new_node_text.clear()
            self.show_dialog(EMPTY_ARGUMENT)
            return

        self.form.new_node_text.clear()

        if self.graph.has_node(new_node):
            self.show_dialog(f"{new_node} is already constructed.")
        else:
            self.graph.add_node(new_node)
            self.form.plot_canvas.plot(self.graph)

    def connect_nodes(self):
        node1 = str(self.form.node1_text.toPlainText())
        node2 = str(self.form.node2_text.toPlainText())
        weight = str(self.form.weight_text.toPlainText())
        self.form.node1_text.clear()
        self.form.node2_text.clear()
        self.form.weight_text.clear()

        if node1 == node2:
            self.show_dialog("Nodes should be different.")
            return

        if not node1 or not node2 or not weight:
            self.show_dialog(EMPTY_ARGUMENT)
            return

        try:
            weight = int(weight)
        except ValueError:
            self.show_dialog("Weight should be an integer.")
            return

        if self.graph.has_edge(node1, node2):
            self.show_dialog(f"Edge: {node1, node2} is already constructed.")
        else:
            self.graph.add_edge(node1, node2, weight=weight)
            self.form.plot_canvas.plot(self.graph)

    def run(self):
        source = str(self.form.source_text.toPlainText())
        dest = str(self.form.destination_text.toPlainText())

        self.form.source_text.clear()
        self.form.destination_text.clear()

        if not source or not dest:
            self.show_dialog(EMPTY_ARGUMENT)
            return

        if self.graph.has_node(source) and self.graph.has_node(dest):
            if source in nx.algorithms.ancestors(self.graph, dest):
                graph = nx.to_dict_of_dicts(self.graph)
                dijkstra = DijkstraAlgorithm(graph)
                parents, visited = dijkstra.find_route(source, dest)
                shortest_path = dijkstra.generate_path(parents, source, dest)
                shortest_path = " -> ".join(shortest_path)
                result = f"Distance is {visited[dest]} units.\nShortest path from {source} to {dest} is {shortest_path}"
                self.form.result_text.setText(result)
                self.form.plot_canvas.plot(self.graph, shortest_path.split(' -> '))
            else:
                self.show_dialog(f"There is no connection between {source} and {dest}.")
        else:
            self.show_dialog("Please check source and destination.")

    def reset(self):
        self.graph = nx.Graph()
        self.form.plot_canvas.plot(self.graph)


def main():
    app = QtWidgets.QApplication([])
    window = GUI()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
