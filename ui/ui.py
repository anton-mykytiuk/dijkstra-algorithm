from PyQt5 import QtCore, QtWidgets
from ui.plot_canvas import PlotCanvas  # Assuming your PlotCanvas class is defined in ui.plot_canvas

ADD_NODE = "Add Node"


class UI(object):

    def __init__(self):
        self.label = None
        self.label_2 = None
        self.label_3 = None
        self.label_4 = None
        self.label_5 = None
        self.label_6 = None
        self.label_7 = None
        self.label_8 = None
        self.label_9 = None
        self.label_10 = None
        self.label_11 = None

        self.line = None
        self.line_2 = None
        self.line_3 = None
        self.line_4 = None

        self.node1_text = None
        self.node2_text = None

        self.error_dialog = None
        self.statusbar = None
        self.menubar = None
        self.reset_graph_button = None
        self.connect_button = None
        self.result_text = None
        self.run_button = None
        self.destination_text = None
        self.source_text = None
        self.weight_text = None
        self.new_node_text = None
        self.add_node_button = None
        self.central_widget = None
        self.plot_canvas = None

    def setup(self, dijkstra_algorithm):
        dijkstra_algorithm.setObjectName("DijkstraAlgorithm")
        dijkstra_algorithm.resize(827, 720)
        self.central_widget = QtWidgets.QWidget(dijkstra_algorithm)
        self.central_widget.setObjectName("central_widget")

        main_layout = QtWidgets.QVBoxLayout(self.central_widget)

        self.plot_canvas = PlotCanvas(self.central_widget)
        self.plot_canvas.setMinimumSize(200, 200)
        main_layout.addWidget(self.plot_canvas)

        controls_layout = QtWidgets.QVBoxLayout()

        input_layout = QtWidgets.QHBoxLayout()

        add_node_layout = QtWidgets.QVBoxLayout()
        self.label_2 = QtWidgets.QLabel(ADD_NODE, self.central_widget)
        add_node_layout.addWidget(self.label_2)
        self.new_node_text = QtWidgets.QTextEdit(self.central_widget)
        self.new_node_text.setMaximumHeight(30)
        add_node_layout.addWidget(self.new_node_text)
        self.add_node_button = QtWidgets.QPushButton(ADD_NODE, self.central_widget)
        add_node_layout.addWidget(self.add_node_button)
        # add_node_layout.addLayout(new_node_layout)
        input_layout.addLayout(add_node_layout)

        input_layout.addWidget(QtWidgets.QFrame(self.central_widget, frameShape=QtWidgets.QFrame.VLine))

        connect_nodes_layout = QtWidgets.QVBoxLayout()
        self.label_3 = QtWidgets.QLabel("Connect Nodes", self.central_widget)
        connect_nodes_layout.addWidget(self.label_3)

        connect_nodes_inputs_layout = QtWidgets.QHBoxLayout()

        node1_layout = QtWidgets.QVBoxLayout()
        self.label_4 = QtWidgets.QLabel("Node 1", self.central_widget)
        node1_layout.addWidget(self.label_4)
        self.node1_text = QtWidgets.QTextEdit(self.central_widget)
        self.node1_text.setMaximumHeight(30)
        node1_layout.addWidget(self.node1_text)
        connect_nodes_inputs_layout.addLayout(node1_layout)

        node2_layout = QtWidgets.QVBoxLayout()
        self.label_5 = QtWidgets.QLabel("Node 2", self.central_widget)
        node2_layout.addWidget(self.label_5)
        self.node2_text = QtWidgets.QTextEdit(self.central_widget)
        self.node2_text.setMaximumHeight(30)
        node2_layout.addWidget(self.node2_text)
        connect_nodes_inputs_layout.addLayout(node2_layout)

        weight_layout = QtWidgets.QVBoxLayout()
        self.label_6 = QtWidgets.QLabel("Weight", self.central_widget)
        weight_layout.addWidget(self.label_6)
        self.weight_text = QtWidgets.QTextEdit(self.central_widget)
        self.weight_text.setMaximumHeight(30)
        weight_layout.addWidget(self.weight_text)
        connect_nodes_inputs_layout.addLayout(weight_layout)

        connect_nodes_layout.addLayout(connect_nodes_inputs_layout)
        self.connect_button = QtWidgets.QPushButton("Connect", self.central_widget)
        connect_nodes_layout.addWidget(self.connect_button)
        input_layout.addLayout(connect_nodes_layout)

        input_layout.addWidget(QtWidgets.QFrame(self.central_widget, frameShape=QtWidgets.QFrame.VLine))

        run_layout = QtWidgets.QVBoxLayout()
        self.label_8 = QtWidgets.QLabel("Run Dijkstra Algorithm", self.central_widget)
        run_layout.addWidget(self.label_8)

        run_inputs_layout = QtWidgets.QHBoxLayout()

        source_layout = QtWidgets.QVBoxLayout()
        self.label_9 = QtWidgets.QLabel("Source", self.central_widget)
        source_layout.addWidget(self.label_9)
        self.source_text = QtWidgets.QTextEdit(self.central_widget)
        self.source_text.setMaximumHeight(30)
        source_layout.addWidget(self.source_text)
        run_inputs_layout.addLayout(source_layout)

        dest_layout = QtWidgets.QVBoxLayout()
        self.label_10 = QtWidgets.QLabel("Destination", self.central_widget)
        dest_layout.addWidget(self.label_10)
        self.destination_text = QtWidgets.QTextEdit(self.central_widget)
        self.destination_text.setMaximumHeight(30)
        dest_layout.addWidget(self.destination_text)
        run_inputs_layout.addLayout(dest_layout)

        run_layout.addLayout(run_inputs_layout)
        self.run_button = QtWidgets.QPushButton("Run", self.central_widget)
        run_layout.addWidget(self.run_button)
        input_layout.addLayout(run_layout)

        controls_layout.addLayout(input_layout)

        result_layout = QtWidgets.QVBoxLayout()
        self.label_11 = QtWidgets.QLabel("Result", self.central_widget)
        result_layout.addWidget(self.label_11)
        self.result_text = QtWidgets.QTextEdit(self.central_widget)
        self.result_text.setReadOnly(True)
        result_layout.addWidget(self.result_text)
        controls_layout.addLayout(result_layout)

        self.reset_graph_button = QtWidgets.QPushButton("Reset Graph", self.central_widget)
        controls_layout.addWidget(self.reset_graph_button)

        main_layout.addLayout(controls_layout)

        dijkstra_algorithm.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(dijkstra_algorithm)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 827, 24))
        self.menubar.setObjectName("menubar")
        dijkstra_algorithm.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(dijkstra_algorithm)
        self.statusbar.setObjectName("statusbar")
        dijkstra_algorithm.setStatusBar(self.statusbar)
        self.error_dialog = QtWidgets.QErrorMessage()

        self.re_translate(dijkstra_algorithm)
        QtCore.QMetaObject.connectSlotsByName(dijkstra_algorithm)

    def re_translate(self, dijkstra_algorithm):
        _translate = QtCore.QCoreApplication.translate
        dijkstra_algorithm.setWindowTitle(_translate("DijkstraAlgorithm", "Dijkstra Algorithm"))
        self.label_2.setText(_translate("DijkstraAlgorithm", "Add Node"))
        self.label_3.setText(_translate("DijkstraAlgorithm", "Connect Nodes"))
        self.label_4.setText(_translate("DijkstraAlgorithm", "Node 1"))
        self.label_5.setText(_translate("DijkstraAlgorithm", "Node 2"))
        self.label_6.setText(_translate("DijkstraAlgorithm", "Weight"))
        self.label_8.setText(_translate("DijkstraAlgorithm", "Run Dijkstra Algorithm"))
        self.label_9.setText(_translate("DijkstraAlgorithm", "Source"))
        self.label_10.setText(_translate("DijkstraAlgorithm", "Destination"))
        self.label_11.setText(_translate("DijkstraAlgorithm", "Result"))
